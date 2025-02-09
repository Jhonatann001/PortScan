PORTSCAN 🚪🔍

PORTSCAN é uma ferramenta simples e eficaz para escanear portas em um endereço IP específico. Desenvolvida em Python, ela verifica quais portas estão abertas em um intervalo de 1 a 1024 (ou vc mesmo escolhe) e exibe os resultados de forma clara e colorida no terminal.

Funcionalidades ✨
Escaneamento de portas TCP em um intervalo de 1 a 1024 por padrão.

Exibição colorida das portas abertas (verde) e fechadas (vermelho).

Interface simples e fácil de usar via linha de comando.


Como Usar 🛠️


Pré-requisitos
Python 3.x instalado.

Biblioteca socket (já inclusa na instalação padrão do Python).


Clone o repositório:
git clone https://github.com/Jhonatann001/portscan.git
cd portscan
python portscan.py
Insira o endereço IP que deseja escanear quando solicitado:


Digite o endereço IP ex: 192.168.0.1:
Aguarde o escaneamento. O resultado será exibido no terminal, destacando as portas abertas em verde e as fechadas em vermelho.

Exemplo de Saída
Após executar o script, você verá algo assim:
![image](https://github.com/user-attachments/assets/e833d921-263c-4fc2-babe-009302308194)

Opções  🚀
Adiciona suporte a escaneamento UDP.

Permitir escaneamento de intervalos de IPs.

Adiciona opção para escanear apenas portas específicas.

Exportar resultados para arquivos TXT.

Adicionar funcionalidade de detecção de serviços em execução nas portas.

Contribuição 🤝
Contribuições são bem-vindas!

Autor 👨‍💻: JHONATAN DE SOUZA 
instagram : @jhonn.souzaa
github : @Jhonatann001


Agradecimentos 🙏
Inspirado por ferramentas como Nmap e outras ferramentas de escaneamento de rede.
