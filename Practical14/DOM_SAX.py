import matplotlib.pyplot as plt

def parse_with_dom(file_path):
    import xml.dom.minidom
    DOMTree = xml.dom.minidom.parse(file_path)
    terms = DOMTree.getElementsByTagName('term')
    molecular_function=0#initialize these variables
    biological_process=0
    cellular_component=0
    for term in terms:
        namespaces = term.getElementsByTagName('namespace')
        for namespace in namespaces:
            #use the for loop to read every namespace
            ontology = namespace.firstChild.nodeValue.strip()
            if ontology == 'molecular_function':
                molecular_function += 1
            elif ontology == 'biological_process':
                biological_process += 1
            elif ontology == 'cellular_component':
                cellular_component += 1
    print("Molecular function (DOM):",molecular_function)
    print("Biological process (DOM):",biological_process)
    print("Cellular component (DOM):",cellular_component)
    lib={'Molecular function':molecular_function,'Biological process':biological_process,'Cellular component':cellular_component}
    import matplotlib.pyplot as plt
    ontologies = list(lib.keys())
    counts=list(lib.values())
    #draw the bar chart
    plt.bar(ontologies, counts, color=['blue', 'green', 'yellow'])
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.title('Number of GO Terms by Ontology (DOM)')
    plt.show()
    return
dom_term_count = parse_with_dom(r'C:\Users\86138\OneDrive - International Campus, Zhejiang University\文档\WeChat Files\wxid_5iwdueoq86yk22\FileStorage\File\2024-05\go_obo.xml')


#now come to the sax part
import xml.sax
# build an empty dictionary for updating 'namespace' elements
ontology_dict = {}
# use the datetime funciton to record the start time and end time in order to calculate the time interval of the process
start_time = datetime.datetime.now()
class GOhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ''
        self.namespace = ''

    # set 'currentdata' to the current element name
    def startElement(self, name, attrs):
        self.currentdata = name

    def endElement(self, name):
        if self.currentdata == 'namespace':
            ontology_name = self.namespace.strip()
            #  update 'ontology_dict' and count the occurance of the different 'namespace's
            ontology_dict[ontology_name] += 1
        else:
            ontology_dict[ontology_name] = 1
            # reset the 'self.namespace' to an empty string in case it carry the previous data to the next namspace 
            self.namespace=''
    # find and accumulate the content of the element : 'namespace'
    def characters(self, content):
        if self.currentdata == 'namespace':
            self.namespace += content

def count_namespace_occurrences(xml_file):
    # create an xml parser and  set its contetnt handler to 'GOhandler'
    handler = GOhandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    # parse the xml file
    parser.parse(xml_file)
    end_time = datetime.datetime.now()
    time_taken = end_time - start_time
    print("Time taken (SAX):", time_taken)
    return ontology_dict
ontology_counts = count_namespace_occurrences("/Users/rickyh/Desktop/go_obo.xml")

print("Namespace Occurances (SAX):", ontology_dict)
import matplotlib.pyplot as plt
ontologies=list(ontology_dict.keys())
counts=list(ontology_dict.values())
plt.bar(ontologies,counts,color=['blue', 'green', 'red'])
plt.xlabel('Ontology')
plt.ylabel('Number of Terms')
plt.title('Number of GO Terms by Ontology (SAX)')
plt.show()

# that show that SAX is faster than DOM
