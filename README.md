# Lume

**Lume** é um utilitário de controle de brilho minimalista, construído em Python, GTK4 e Libadwaita para Linux. Focado na filosofia "abrir, ajustar no slider e fechar", ele visa simplicidade extrema sem perder poder. 

O Lume possui suporte universal: controla de forma fluida tanto monitores embutidos (telas de Notebooks) via `sysfs`, quanto múltiplos monitores externos conectados via HDMI/DisplayPort através do protocolo DDC/CI (usando `ddcutil`).

## Instalação

A maneira mais fácil e recomendada de instalar o Lume é utilizando os instaladores nativos. Eles já baixam e configuram tudo (Python, GTK4, dependências) sem que você precise se preocupar.

### Ubuntu, Linux Mint, Debian (.deb)
Baixe o arquivo `.deb` mais recente na aba **Releases** do GitHub e instale com dois cliques. Se preferir pelo terminal:
```bash
sudo apt install ./lume_1.0.0-1_all.deb
```

### Fedora, CentOS, openSUSE (.rpm)
Baixe o arquivo `.rpm` mais recente na aba **Releases** do GitHub e instale com dois cliques. Via terminal:
```bash
sudo dnf install ./lume-1.0.0-1.noarch.rpm
```

---

## Recursos Principais
- **Design Minimalista:** Integração nativa com o ecossistema GNOME (GTK4 + Libadwaita).
- **Controle Simultâneo:** Deslize o brilho de várias telas ao mesmo tempo de forma assíncrona, sem o app travar ou engasgar.
- **Detecção Inteligente:** O aplicativo faz cache dos monitores externos e sincroniza o hardware instantaneamente assim que abre.
- **Rotinas Automáticas:** Um *Daemon* invisível embutido permite agendar trocas de brilho independentes para cada monitor em horários específicos.

## Dúvidas Frequentes (Permissões)
Para controlar monitores externos, o Linux exige permissões especiais no barramento i2c. Os pacotes `.deb` e `.rpm` fornecidos acima já instalam automaticamente as regras corretas de *udev*. Caso seus monitores externos não apareçam na primeira vez, **reinicie o computador** para que o grupo de vídeo seja aplicado ao seu usuário.

## Empacotamento a partir da Fonte (Desenvolvedores)

Se você clonou este repositório e deseja compilar o seu próprio instalador localmente:

**Gerar pacote .deb (Ubuntu/Debian):**
```bash
sudo apt install devscripts debhelper
dpkg-buildpackage -us -uc -b
```

**Gerar pacote .rpm (Fedora/RedHat):**
```bash
rpmbuild -ba lume.spec
```
