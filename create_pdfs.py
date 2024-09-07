import os
import re
import markdown2
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import git

def clone_or_pull_repo(repo_url, local_path):
    if os.path.exists(local_path):
        repo = git.Repo(local_path)
        origin = repo.remotes.origin
        origin.pull()
        print(f"Pulled latest changes from {repo_url}")
    else:
        git.Repo.clone_from(repo_url, local_path)
        print(f"Cloned repository from {repo_url}")

def parse_summary(summary_path):
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = re.findall(r'\* \[(.*?)\]\((.*?)\)', content)
    folder_structure = {}

    for section, path in sections:
        folder_name = os.path.dirname(path)
        if folder_name not in folder_structure:
            folder_structure[folder_name] = []
        folder_structure[folder_name].append(path)

    return folder_structure

def markdown_to_html(md_content):
    return markdown2.markdown(md_content, extras=['fenced-code-blocks', 'tables'])

def create_pdf(folder_name, file_paths, output_dir, repo_path):
    html_content = f"<h1>{folder_name}</h1>"
    
    for file_path in file_paths:
        full_path = os.path.join(repo_path, file_path)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            html_content += markdown_to_html(md_content)
        else:
            print(f"Warning: File not found - {full_path}")

    font_config = FontConfiguration()
    css = CSS(string='''
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body { 
            font-family: 'Roboto', sans-serif; 
            font-size: 12px;
            line-height: 1.6;
            word-wrap: break-word;
        }
        h1, h2, h3 { color: #333; }
        code { 
            background-color: #f0f0f0; 
            padding: 2px 4px; 
            border-radius: 4px; 
            font-size: 0.9em;
        }
        pre { 
            background-color: #f0f0f0; 
            padding: 10px; 
            border-radius: 4px; 
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        @page {
            margin: 1cm;
        }
    ''', font_config=font_config)

    output_path = os.path.join(output_dir, f"{folder_name}.pdf")
    HTML(string=html_content).write_pdf(output_path, stylesheets=[css], font_config=font_config)
    print(f"Created PDF: {output_path}")

def main():
    repo_url = "https://github.com/ashwinknan/testterra.git"
    local_repo_path = os.path.join(os.path.dirname(__file__), "repo_files")
    output_dir = 'output_pdfs'
    os.makedirs(output_dir, exist_ok=True)

    clone_or_pull_repo(repo_url, local_repo_path)

    summary_path = os.path.join(local_repo_path, 'SUMMARY.md')
    folder_structure = parse_summary(summary_path)

    for folder_name, file_paths in folder_structure.items():
        create_pdf(folder_name, file_paths, output_dir, local_repo_path)

if __name__ == "__main__":
    main()
