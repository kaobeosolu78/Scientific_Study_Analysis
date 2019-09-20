import pickle

# loads pickled files
def load_obj(datatype):
    with open("{}".format(datatype) + '.pkl', 'rb') as f:
        return pickle.load(f)


class studies:
    def __init__(self,kw,all=[]):
        self.key = kw
        self.all_studies = all

    def add_study(self,stud):
        self.all_studies.append(stud)
        
    def get_titles(self):
        self.titles = [item.title for item in self.all_studies]
        return self.titles

class study:
    def __init__(self,title,content):
        self.title = title
        self.rawcont = content
        
    def get_section(self,section):
        for k in range(len(list(self.rawcont.keys()))):
            if list(self.rawcont.keys())[k] in section or list(self.rawcont.keys())[k] in section.upper():
                return self.rawcont[list(self.rawcont.keys())[k]]
            
    def combine_text(self,exclude=[]):
        self.combined = ""
        for key in list(self.rawcont.keys()):
            if key not in exclude:
                self.combined += " " + self.rawcont[key]
        return self.combined