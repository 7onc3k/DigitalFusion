import os

class Config:
    def __init__(self):
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.src_dir = os.path.join(self.project_dir, "src")
        self.log_level = "INFO"
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY", "sk-d5065d503a9a47008e8589f3d570328c")
        self.deepseek_api_url = "https://api.deepseek.com/chat/completions"
        self.file_extensions = [".tsx", ".js", ".ts", ".css", ".astro", ".py", ".json"]
        self.include_config_files = True
        self.config_files = ['.env', '.env.local', 'package.json', 'tsconfig.json', 'next.config.js', 'next.config.mjs']
        self.append_to_clipboard = False
        self.repository_map_file = os.path.join(self.project_dir, "repository_map.json")

    def __str__(self):
        return f"Config(project_dir={self.project_dir}, src_dir={self.src_dir})"
