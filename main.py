def extract():
    import etl.extract

def transform():
    import etl.transform

def load():
    import etl.load

def analysis():
    import analysis.model
    import analysis.evaluate

def visualization():
    import vis.visualizations

if __name__ == "__main__":
    extract()
    transform()
    load()
    analysis()
    visualization()
    print("Analysis completed successfully.")
