class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value or ""
    
        attrs_str = ""
        if self.props:
            for attr, value in self.props.items():
                attrs_str += f' {attr}="{value}"'
    
        if self.children is None:
            if self.value:
                return f"<{self.tag}{attrs_str}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{attrs_str}/>"
    
        children_html = ""
        if self.children:
            for child in self.children:
                children_html += child.to_html()
    
        if self.value:
            children_html = self.value + children_html
    
        return f"<{self.tag}{attrs_str}>{children_html}</{self.tag}>"

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        else:
            html_list = [] 
            for key,value in self.props.items():
                html_list.append(f' {key}="{value}"')
            return "".join(html_list)

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        attributes_html = ""
        if self.props:
            for key, value in self.props.items():
                attributes_html += f' {key}="{value}"'
        return f"<{self.tag}{attributes_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        if self.children is None:
            raise ValueError("ParentNode children cannot be None")
        else:
            html_string = f"<{self.tag}>" 
            for child in self.children:
                html_string += child.to_html()
            html_string += f"</{self.tag}>"
            return html_string
