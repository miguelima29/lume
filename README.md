# Lume

Lume é um utilitário de controle de brilho minimalista, construído em Python, GTK4 e Libadwaita para Linux. Focado na filosofia "abrir, ajustar no slider e fechar", ele visa simplicidade extrema sem perder poder.

Lume tem suporte tanto para monitores embutidos (Notebooks) via `sysfs`, quanto para múltiplos monitores externos através do protocolo DDC/CI (usando `ddcutil`).

## Recursos Principais
- **Design Minimalista:** Integração nativa com o ecossistema GNOME (GTK4 + Libadwaita).
- **Controle Simultâneo:** Deslize o brilho de várias telas ao mesmo tempo de forma assíncrona, sem gargalos.
- **Detecção Inteligente:** O backend faz cache dos monitores externos e sincroniza o hardware instantaneamente.
- **Rotinas Automáticas:** Um *Daemon* de segundo plano embutido permite agendar trocas de brilho por monitor em horários específicos.

## Permissões (DDC/CI)
Para controlar monitores externos sem ser root, as regras udev instaladas pelo pacote dão acesso aos usuários do grupo `video` ou à sessão atual.

## Como Compilar e Empacotar

O Lume possui estrutura nativa para as duas maiores famílias de distribuições Linux:

### 1. Ubuntu, Linux Mint, Debian (.deb)
Para compilar o pacote `.deb`:
```bash
sudo apt install devscripts debhelper
dpkg-buildpackage -us -uc -b
```
Isso irá gerar um arquivo `.deb` no diretório anterior, que pode ser instalado com:
```bash
sudo apt install ../lume_1.0.0-1_all.deb
```

### 2. Fedora, RHEL, openSUSE (.rpm)
Para compilar o pacote `.rpm`:
```bash
rpmbuild -ba lume.spec
```
Isso irá gerar o pacote no seu diretório `~/rpmbuild/RPMS/`.
