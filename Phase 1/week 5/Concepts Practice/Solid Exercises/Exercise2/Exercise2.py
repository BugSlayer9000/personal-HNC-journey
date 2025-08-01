# samod subhasha


# Exercise 2: Document Generator (Liskov Substitution & Interface Segregation)
    # Create a document generation system for PDF, Word, and HTML formats. Focus on:

        # Ensuring derived classes can replace base classes without breaking functionality (Liskov Substitution Principle - LSP)
        # Creating focused interfaces rather than one large interface (Interface Segregation Principle - ISP)

# Document Genarator

from abc import ABC, abstractmethod

class IDocumentGenerator(ABC): # Genaral interface all document generators implement
    
    @abstractmethod
    def generate(self, content:str) -> str:
        pass
    

class IWatermarkable(ABC): # Only pdf and work omplement this 
    
    @abstractmethod
    def add_watermark(self, watermark_text: str) -> str:
        pass
    
class IStylable(ABC): # only wokrd and html implement this
    
    @abstractmethod
    def set_style(self, style:dict) -> None:
        pass


class PDFGenerator(IDocumentGenerator, IWatermarkable):
    def __init__(self, file_path:str,  ) -> None:
        self._file_path = file_path
        self._watermark_text = ""
    
    def generate(self, content: str):
        return f"PDF Document Genarated ! \n{content}"

    def add_watermark(self, watermark_text: str) -> str:
        self._watermark_text = watermark_text
        return f"Water mark aded ! - watermark - {watermark_text}"

class WordGenerator(IDocumentGenerator, IWatermarkable, IStylable):
    def __init__(self, file_path:str) -> None:
        self._file_path = file_path
        self._style = dict
        self._watermark = ""
    
    def generate(self, content: str) -> str:
        return f"Word Document Genarated ! \n{content}"
    
    def add_watermark(self, watermark_text: str) -> str:
        self._watermark = watermark_text
        return f"Water mark aded ! - watermark - {watermark_text}"
    
    def set_style(self, style: dict) -> None:
        self._style = style
    
    

class HTMLGenerator(IDocumentGenerator, IStylable):
    def __init__(self, template_path:str) -> None:
        self._template_path = template_path
        self._style = dict
    
    def generate(self, content: str) -> str:
        return f"HTML doc genarated"
    
    def set_style(self, style: dict) -> None:
        self._style = style
        
    
    


def main():
    # Test Data
    content = "This is a test invoice.\nAmount Due: $299.99"
    watermark = "CONFIDENTIAL"
    style = {
        "font": "Arial",
        "font_size": 12,
        "color": "#333"
    }

    # PDF Test
    pdf_generator = PDFGenerator("/docs/invoice.pdf",)
    pdf_generator.add_watermark(watermark)
    pdf_output = pdf_generator.generate(content)
    print("PDF Output:\n", pdf_output)

    # Word Test
    word_generator = WordGenerator("/docs/invoice.docx")
    word_generator.set_style(style)
    word_generator.add_watermark(watermark)
    word_output = word_generator.generate(content)
    print("Word Output:\n", word_output)

    # HTML Test
    html_generator = HTMLGenerator("/templates/invoice.html")
    html_generator.set_style(style)
    html_output = html_generator.generate(content)
    print("HTML Output:\n", html_output)

    # LSP Test: All generators used through same interface
    def render_document(generator: IDocumentGenerator):
        return generator.generate("LSP compliance test.")

    print(render_document(pdf_generator))   # Should not raise
    print(render_document(word_generator))  # Should not raise
    print(render_document(html_generator))  # Should not raise

main()


