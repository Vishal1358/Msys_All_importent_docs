import configparser


def get_data():
    config = configparser.ConfigParser()
    config.read(r'D:\Product-Compare-Muti-Sites\Configure\ConfigFile.ini')
    f_url=config.get("db", "flipkart_url")
    a_url=config.get("db", "amazon_url")
    c_url=config.get("db", "croma_url")
    remote_url=config.get("db", "remote_executer")
    return f_url,a_url,c_url,remote_url

