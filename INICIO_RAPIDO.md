# Lab Cripto - Guia Rápido em Português 🇵🇹

## Correr a Aplicação

### Opção 1: A Forma Mais Fácil (Recomendado)
Simplesmente **clica duas vezes** no ficheiro `run.bat` que está na pasta do projeto.

### Opção 2: Linha de Comando
Abre o Command Prompt ou PowerShell na pasta do projeto e executa:

```cmd
run.bat
```

Ou usa Python diretamente:

```cmd
py main.py
```

## Criar um Executável (.exe)

### Opção 1: A Forma Mais Fácil
Clica duas vezes no ficheiro `build.bat`.

O programa vai criar um ficheiro `lab_cripto.exe` na pasta `dist/`.

### Opção 2: Linha de Comando
```cmd
build.bat
```

Ou usa Python com PyInstaller diretamente:

```cmd
py -m PyInstaller lab_cripto_new.spec
```

## Testar os Ciphers

Para ver exemplos de todos os ciphers funcionando:

```cmd
py example_usage.py
```

## Estrutura do Projeto

```
lab_cripto/
├── main.py                    # Ficheiro principal
├── INICIO_RAPIDO.md          # Este ficheiro
├── LICENSE                    # Licença MIT
├── CHANGELOG.md               # Histórico de versões
├── CONTRIBUTING.md            # Como contribuir correr (DUPLO CLIQUE!)
├── build.bat                  # Script para compilar (.exe)
├── example_usage.py           # Exemplos de uso
├── requirements.txt           # Dependências
├── README.md                  # Documentação em inglês
├── SETUP_WINDOWS.md          # Guia de setup completo
├── LICENSE                    # Licença MIT
└── src/
    ├── ciphers/              # 6 tipos de criptografia
    └── ui/                   # Interface gráfica
```

## Problemas Comuns

### Erro: "Python was not found"
**Solução:** Usa o ficheiro `run.bat` em vez de tentar escrever `python` manualmente.

### Erro: "pyinstaller: The term 'pyinstaller' is not recognized"
**Solução:** Usa o ficheiro `build.bat` em vez de escrever pyinstaller manualmente.

### Erro: "ModuleNotFoundError"
**Solução:** Verifica se Python está instalado corretamente.

## Documentação Completa

- **README.md** - Documentação técnica em inglês
- **SETUP_WINDOWS.md** - Guia completo de setup para Windows
- **DEVELOPMENT.md** - Notas de desenvolvimento
- **CHANGELOG.md** - Histórico de versões
- **CONTRIBUTING.md** - Como contribuir

## Resumo
`run.bat` ou `py main.py` |
| Criar .exe | `build.bat` |
| Testar ciphers | `py
| Correr a app | Duplo clique em `run.bat` |
| Criar .exe | Duplo clique em `build.bat` |
| Testar ciphers | `python example_usage.py` |
| Ver documentação | Abre `README.md` |

---

**Tudo pronto para publicar no GitHub!** 🎉
