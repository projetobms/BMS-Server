#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

// Função para dividir a string e converter para double
void parse_doubles(const char *str, double *arr, int *count) {
    char *token;
    char *end;
    char buffer[BUFFER_SIZE];
    strcpy(buffer, str);  // Copiar a string para não modificar o original
    *count = 0;

    // Separar a string com base no delimitador ':'
    token = strtok(buffer, ":");
    while (token != NULL) {
        arr[*count] = strtod(token, &end);  // Converter cada parte para double
        (*count)++;
        token = strtok(NULL, ":");  // Próximo token
    }
}

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    int valread;
    double values[BUFFER_SIZE];  // Vetor para armazenar os valores double
    int num_values;  // Quantidade de valores convertidos

    // Criar o socket do servidor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }

    // Configurar opções do socket
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    
    // Definir o endereço e porta do servidor
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Vincular o socket à porta
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Colocar o servidor para escutar por conexões
    if (listen(server_fd, 3) < 0) {
        perror("Listen");
        exit(EXIT_FAILURE);
    }

    printf("Servidor TCP aguardando conexões na porta %d...\n", PORT);
    fflush(stdout);

    // Aceitar conexão
    while ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) >= 0) {
        printf("Conexão estabelecida com um cliente!\n");
        fflush(stdout);

        // Continuar lendo pacotes enquanto a conexão estiver ativa
        while ((valread = read(new_socket, buffer, BUFFER_SIZE)) > 0) {
            buffer[valread] = '\0';  // Garantir que a string está corretamente terminada
            printf("Mensagem recebida: %s\n", buffer);
            fflush(stdout);

            // Converter a string recebida em um vetor de doubles
            parse_doubles(buffer, values, &num_values);

            // Imprimir os valores convertidos
            printf("Valores convertidos:\n");
            for (int i = 0; i < num_values; i++) {
                printf("%f\n", values[i]);
            }
            fflush(stdout);
        }

        // Se a conexão for encerrada
        if (valread == 0) {
            printf("Conexão encerrada pelo cliente.\n");
            fflush(stdout);
        } else if (valread < 0) {
            perror("Erro na leitura");
        }
        
        // Fechar o socket do cliente após o término da comunicação
        close(new_socket);
    }

    if (new_socket < 0) {
        perror("Accept");
        exit(EXIT_FAILURE);
    }

    return 0;
}
