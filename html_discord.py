

def parse(soup):
    '''
        replace
    <strong>=**
    <em>=*
    <span style=\"text-decoration: underline;\">=__
    <span style=\"text-decoration: line-through;\">=~~
    
        remove
    <br/>
    <p>
    <span style=\"color:white\">
    <span class=\"printuser avatarhover\">
    <a href=\"\">
    '''
    para=[]
    unrecognised=[]
    for i in soup:
        if len(i)-1 and str(i)[:3]!='<p>':
            parsed=parse(i)
            if parsed[0]!=[]:
                para+=parsed[0]
            if parsed[1]!=[]:
                unrecognised+=parsed[1]
        else:
            if str(i)[:3]=='<p>':
                string=str(i)
                string=string.replace('<strong>','**')
                string=string.replace('</strong>','**')
                string=string.replace('<em>','*')
                string=string.replace('</em>','*')
                string=string.replace('<br/>','')
                string=string.replace('<p>','')
                string=string.replace('</p>','')
                while string.find('<span')+1:
                    pos=string.find('<span')
                    new_pos=string[1+pos:].find('>')
                    tag=string[pos:new_pos+pos+2]
                    if tag=='<span style=\"text-decoration: underline;\">':
                        string=string.replace(tag,'__',1)
                        string=string.replace('</span>','__',1)
                    elif tag=='<span style=\"text-decoration: line-through;\">':
                        string=string.replace(tag,'~~',1)
                        string=string.replace('</span>','~~',1)
                    elif tag=='':
                        print('tag is blank?')
                        print('pos=',pos,'new_pos=',new_pos)
                        print('string',string)
                        kill
                    else:
                        #print(f'Unrecognised tag: {tag}')
                        string=string.replace(tag,'',1)
                        string=string.replace('</span>','',1)
                        unrecognised.append(tag)
                while string.find('<a')+1:
                    pos=string.find('<a')
                    new_pos=string[1+pos:].find('>')
                    tag=string[pos:new_pos+pos+2]
                    if tag=='':
                        print('tag is blank?')
                        print('pos=',pos,'new_pos=',new_pos)
                        print('string',string)
                        kill
                    string=string.replace(tag,'',1)
                    string=string.replace('</a>','',1)
                while string.find('<')+1:
                    pos=string.find('<')
                    new_pos=string[1+pos:].find('>')
                    tag=string[pos:new_pos+pos+2]
                    unrecognised.append(tag)
                    a_pos=string[pos+new_pos+2:].find('<')
                    a_new_pos=string[pos+new_pos+2+a_pos:].find('>')
                    a_tag=string[pos+new_pos+2+a_pos:pos+new_pos+2+a_pos+a_new_pos+1]
                    string=string.replace(tag,'',1)
                    string=string.replace(a_tag,'',1)
                    
                para.append(string)
    return [para,unrecognised]

def test(string):
    pos=string.find('<')
    new_pos=string[1+pos:].find('>')
    tag=string[pos:new_pos+pos+2]
    #unrecognised.append(tag)
    a_pos=string[pos+new_pos+2:].find('<')
    a_new_pos=string[pos+new_pos+2+a_pos:].find('>')
    a_tag=string[pos+new_pos+2+a_pos:pos+new_pos+2+a_pos+a_new_pos+1]
    print(tag)
    print(a_tag)

def send(string):
    strings=[]
    if len(string)<2000:
        strings.append(string)
    else:
        line=''
        while len(string):
            dot_finder=string.find('.')
            
            if dot_finder+1:
                #if there is a sentence with fullstop
                if len(line)+dot_finder<2000:
                    #add the sentence to line
                    line+=string[:dot_finder+1]
                    string=string[dot_finder+1:]
                else:
                    #send the line
                    strings.append(line)
                    line=''
            else:
                #if there is not sentence with fullstop
                if len(line)+len(string)<2000:
                    #send the line+string
                    line+=string
                    strings.append(line)
                    line=''
                    string=''
                else:
                    #send the line then string in message after
                    strings.append(line)
                    strings.append(string)
                    line=''
                    string=''
    return strings