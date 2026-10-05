# PDF Extractor

Ferramenta Python para extrair **texto, imagens, metadados e propriedades tipográficas** de arquivos PDF usando PyMuPDF. Oferece uma classe reutilizável e uma interface de linha de comando para selecionar páginas e organizar os arquivos de saída.

## Funcionalidades

- Extrair o texto do documento por página.
- Salvar imagens incorporadas ao PDF.
- Identificar nome, tamanho e cor das fontes presentes nos trechos de texto.
- Extrair os metadados disponíveis no documento.
- Processar todas as páginas ou uma seleção específica.

## Instalação

```bash
git clone https://github.com/JonasChristiano/pdf-extractor.git
cd pdf-extractor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows, ative o ambiente com `.venv\Scripts\Activate.ps1` no PowerShell.

## Uso pela linha de comando

```bash
# Extrair todas as informações.
python pdf_extract.py documento.pdf --extract all --output_folder resultado

# Extrair o texto das páginas 1 e 2.
python pdf_extract.py documento.pdf --extract text --pages 1 2 --output_folder resultado

# Extrair apenas imagens ou metadados.
python pdf_extract.py documento.pdf --extract images --output_folder resultado
python pdf_extract.py documento.pdf --extract metadata --output_folder resultado

# Consultar as opções disponíveis.
python pdf_extract.py --help
```

As páginas são informadas a partir de **1**. O parâmetro `--extract` aceita `images`, `fonts`, `text`, `metadata` ou `all`. Quando `--output_folder` não é informado, a saída fica em `pdf_extract/`, no diretório de execução.

## Uso em Python

```python
from pdf_extract import PDFExtractor

extractor = PDFExtractor("documento.pdf", "resultado")
try:
    extractor.extract_text(pages=[1, 2])
    extractor.extract_metadata()
finally:
    extractor.pdf_document.close()
```

## Arquivos gerados

```text
resultado/
├── text.txt
├── metadata.txt
├── font_styles.txt
└── images/
    └── page1_img1.png
```

Os arquivos dependem das opções escolhidas; a extensão das imagens acompanha seu formato no PDF. Os arquivos de texto da mesma pasta são substituídos em uma nova extração, portanto use pastas distintas para documentos diferentes.

## Escopo atual

O projeto extrai conteúdo já presente no PDF. Reconhecimento de texto por OCR, processamento em lote e recuperação automática de arquivos inválidos não fazem parte da implementação atual. O nome e o conteúdo dos metadados dependem do documento de origem.

## Estrutura

- `pdf_extract.py`: classe de extração e interface CLI.
- `requirements.txt`: dependências da versão do projeto.
- `setup.py`: metadados de distribuição.

## Contribuição e licença

Sugestões, correções e exemplos de uso são bem-vindos via issues e pull requests. Ao relatar um problema, informe a opção utilizada e o erro; utilize um PDF de exemplo que possa ser compartilhado.

Licença [MIT](LICENSE). Desenvolvido por [Jonas Christiano](https://github.com/JonasChristiano).
