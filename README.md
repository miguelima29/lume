# Lume

Lume é um utilitário de controle de brilho minimalista, construído em Python, GTK4 e Libadwaita para Linux. Focado na filosofia "abrir, ajustar no slider e fechar", ele visa simplicidade extrema sem perder poder.

Lume tem suporte tanto para monitores embutidos (Notebooks) via `sysfs`, quanto para múltiplos monitores externos através do protocolo DDC/CI (usando `ddcutil`).

## Recursos Principais
- **Design Minimalista:** Integração nativa com o ecossistema GNOME (GTK4 + Libadwaita).
- **Controle Simultâneo:** Deslize o brilho de várias telas ao mesmo tempo de forma assíncrona, sem gargalos.
- **Detecção Inteligente:** O backend faz cache dos monitores externos e sincroniza o hardware instantaneamente.
- **Rotinas Automáticas:** Um *Daemon* de segundo plano embutido permite agendar trocas de brilho por monitor em horários específicos.

## Pré-requisitos
Para rodar o Lume localmente ou compilá-lo:
* `python3` e `python3-gobject`
* `gtk4` e `libadwaita`
* `ddcutil`

## Permissões
Para controlar monitores externos sem ser root, seu usuário precisa ter acesso ao barramento i2c.
As regras udev incluídas no projeto já dão acesso aos usuários do grupo `video` ou à sessão atual.

## Como Executar
```bash
python3 lume
```

## Empacotamento
O projeto possui um arquivo `lume.spec` para build nativo em RPM (Fedora, RHEL, openSUSE).
Para construir o pacote:
```bash
rpmbuild -ba lume.spec
```
