def parse_with_dom(file_path):
    import xml.dom.minidom
    DOMTree = xml.dom.minidom.parse(file_path)
    terms = DOMTree.getElementsByTagName('term')
    molecular_function=0
    biological_process=0
    cellular_component=0
    for term in terms:
        namespaces = term.getElementsByTagName('namespace')
        for namespace in namespaces:
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
    plt.bar(ontologies, counts, color=['blue', 'green', 'red'])
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.title('Number of GO Terms by Ontology (DOM)')
    plt.show()
    return
dom_term_count = parse_with_dom(r'C:\Users\86138\OneDrive - International Campus, Zhejiang University\文档\WeChat Files\wxid_5iwdueoq86yk22\FileStorage\File\2024-05\go_obo.xml')