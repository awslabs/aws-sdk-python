from datetime import datetime


def on_config(config, **kwargs):
    config.copyright = f"Copyright &copy; {datetime.now().year}, Amazon Web Services, Inc"
    return config
