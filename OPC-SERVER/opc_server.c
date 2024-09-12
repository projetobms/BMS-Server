#include <signal.h>
#include <open62541/server.h>
#include <open62541/server_config_default.h>

UA_Boolean running = true;

void signalHandler(int sig) {
    running = false;
}

int main(int argc, char** argv)
{
    signal(SIGINT, signalHandler); /* capturar ctrl-c */

    /* Criar um servidor ouvindo na porta 4840 */
    UA_Server *server = UA_Server_new();
    UA_ServerConfig *config = UA_Server_getConfig(server);

    /* Configurar o servidor para escutar em todos os endereços IP e sem segurança */
    UA_ServerConfig_setMinimal(config, 4840, NULL);

    /* Configurar o modo de segurança para "None" (sem segurança) */
    config->endpoints[0].securityMode = UA_MESSAGESECURITYMODE_NONE;

    UA_NodeId parentNodeId = UA_NODEID_NUMERIC(0,UA_NS0ID_OBJECTSFOLDER);
    UA_NodeId parentReferenceNodeId = UA_NODEID_NUMERIC(0,UA_NS0ID_ORGANIZES);
    UA_NodeId variableType = UA_NODEID_NULL;


    /* Adicionar o nó de variável batteryVoltage */
    /* 1) Definir os atributos do nó */
    UA_VariableAttributes batteryVoltageAttr = UA_VariableAttributes_default;
    
    batteryVoltageAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryVoltageAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryVoltage");
    UA_Double batteryVoltage = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryVoltageAttr.value, &batteryVoltage, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryVoltageNodeId = UA_NODEID_STRING(1, "battery.voltage");
    UA_QualifiedName batteryVoltageBrowseName = UA_QUALIFIEDNAME(1, "batteryVoltage");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryVoltageNodeId, parentNodeId, parentReferenceNodeId,
                              batteryVoltageBrowseName, variableType, batteryVoltageAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes batteryTemperatureAttr = UA_VariableAttributes_default;
    
    batteryTemperatureAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryTemperatureAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryTemperature");
    UA_Double batteryTemperature = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryTemperatureAttr.value, &batteryTemperature, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryTemperatureNodeId = UA_NODEID_STRING(2, "battery.temperature");
    UA_QualifiedName batteryTemperatureBrowseName = UA_QUALIFIEDNAME(2, "batteryTemperature");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryTemperatureNodeId, parentNodeId, parentReferenceNodeId,
                              batteryTemperatureBrowseName, variableType, batteryTemperatureAttr, NULL, NULL);
    
    /*------------------------------------------------------------------------------------------*/

    
    UA_VariableAttributes batteryCurrentAttr = UA_VariableAttributes_default;
    
    batteryCurrentAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryCurrentAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryCurrent");
    UA_Double batteryCurrent = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryCurrentAttr.value, &batteryCurrent, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryCurrentNodeId = UA_NODEID_STRING(3, "battery.current");
    UA_QualifiedName batteryCurrentBrowseName = UA_QUALIFIEDNAME(3, "batteryCurrent");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryCurrentNodeId, parentNodeId, parentReferenceNodeId,
                              batteryCurrentBrowseName, variableType, batteryCurrentAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes batterySOCAttr = UA_VariableAttributes_default;
    
    batterySOCAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batterySOCAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batterySOC");
    UA_Double batterySOC = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batterySOCAttr.value, &batterySOC, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batterySOCNodeId = UA_NODEID_STRING(4, "battery.SOC");
    UA_QualifiedName batterySOCBrowseName = UA_QUALIFIEDNAME(4, "batterySOC");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batterySOCNodeId, parentNodeId, parentReferenceNodeId,
                              batterySOCBrowseName, variableType, batterySOCAttr, NULL, NULL);
    
    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes batteryDischargeCurrentAttr = UA_VariableAttributes_default;
    
    batteryDischargeCurrentAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryDischargeCurrentAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryDischargeCurrent");
    UA_Double batteryDischargeCurrent = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryDischargeCurrentAttr.value, &batteryDischargeCurrent, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryDischargeCurrentNodeId = UA_NODEID_STRING(5, "battery.dischargecurrent");
    UA_QualifiedName batteryDischargeCurrentBrowseName = UA_QUALIFIEDNAME(5, "batteryDischargeCurrent");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryDischargeCurrentNodeId, parentNodeId, parentReferenceNodeId,
                              batteryDischargeCurrentBrowseName, variableType, batteryDischargeCurrentAttr, NULL, NULL);
    
    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes batteryChargerVoltageAttr = UA_VariableAttributes_default;
    
    batteryChargerVoltageAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryChargerVoltageAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryChargerVoltage");
    UA_Double batteryChargerVoltage = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryChargerVoltageAttr.value, &batteryChargerVoltage, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryChargerVoltageNodeId = UA_NODEID_STRING(6, "battery.chargervoltage");
    UA_QualifiedName batteryChargerVoltageBrowseName = UA_QUALIFIEDNAME(6, "batteryChargerVoltage");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryChargerVoltageNodeId, parentNodeId, parentReferenceNodeId,
                              batteryChargerVoltageBrowseName, variableType, batteryChargerVoltageAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes batteryChargerEnableAttr = UA_VariableAttributes_default;
    
    batteryChargerEnableAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryChargerEnableAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryChargerEnable");
    UA_Double batteryChargerEnable = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryChargerEnableAttr.value, &batteryChargerEnable, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryChargerEnableNodeId = UA_NODEID_STRING(7, "battery.chargerenable");
    UA_QualifiedName batteryChargerEnableBrowseName = UA_QUALIFIEDNAME(7, "batteryChargerEnable");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryChargerEnableNodeId, parentNodeId, parentReferenceNodeId,
                              batteryChargerEnableBrowseName, variableType, batteryChargerEnableAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes batteryDischargerEnableAttr = UA_VariableAttributes_default;
    
    batteryDischargerEnableAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    batteryDischargerEnableAttr.displayName = UA_LOCALIZEDTEXT("en-US", "batteryDischargerEnable");
    UA_Double batteryDischargerEnable = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&batteryDischargerEnableAttr.value, &batteryDischargerEnable, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId batteryDischargerEnableNodeId = UA_NODEID_STRING(8, "battery.dischargerenable");
    UA_QualifiedName batteryDischargerEnableBrowseName = UA_QUALIFIEDNAME(8, "batteryDischargerEnable");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, batteryDischargerEnableNodeId, parentNodeId, parentReferenceNodeId,
                              batteryDischargerEnableBrowseName, variableType, batteryDischargerEnableAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes chamberSetpointAttr = UA_VariableAttributes_default;
    
    chamberSetpointAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    chamberSetpointAttr.displayName = UA_LOCALIZEDTEXT("en-US", "chamberSetpoint");
    UA_Double chamberSetpointEnable = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&chamberSetpointAttr.value, &chamberSetpointEnable, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId chamberSetpointNodeId = UA_NODEID_STRING(9, "chamber.setpoint");
    UA_QualifiedName chamberSetpointBrowseName = UA_QUALIFIEDNAME(9, "chamberSetpoint");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, chamberSetpointNodeId, parentNodeId, parentReferenceNodeId,
                              chamberSetpointBrowseName, variableType, chamberSetpointAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/
    UA_VariableAttributes espBatteryVoltageAttr = UA_VariableAttributes_default;
    
    espBatteryVoltageAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryVoltageAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryVoltage");
    UA_Double espBatteryVoltage = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryVoltageAttr.value, &espBatteryVoltage, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryVoltageNodeId = UA_NODEID_STRING(11, "esp.battery.voltage");
    UA_QualifiedName espBatteryVoltageBrowseName = UA_QUALIFIEDNAME(11, "espBatteryVoltage");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryVoltageNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryVoltageBrowseName, variableType, espBatteryVoltageAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes espBatteryTemperatureAttr = UA_VariableAttributes_default;
    
    espBatteryTemperatureAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryTemperatureAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryTemperature");
    UA_Double espBatteryTemperature = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryTemperatureAttr.value, &espBatteryTemperature, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryTemperatureNodeId = UA_NODEID_STRING(12, "esp.battery.temperature");
    UA_QualifiedName espBatteryTemperatureBrowseName = UA_QUALIFIEDNAME(12, "espBatteryTemperature");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryTemperatureNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryTemperatureBrowseName, variableType, espBatteryTemperatureAttr, NULL, NULL);
    
    /*------------------------------------------------------------------------------------------*/

    
    UA_VariableAttributes espBatteryCurrentAttr = UA_VariableAttributes_default;
    
    espBatteryCurrentAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryCurrentAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryCurrent");
    UA_Double espBatteryCurrent = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryCurrentAttr.value, &espBatteryCurrent, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryCurrentNodeId = UA_NODEID_STRING(13, "esp.battery.current");
    UA_QualifiedName espBatteryCurrentBrowseName = UA_QUALIFIEDNAME(13, "espBatteryCurrent");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryCurrentNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryCurrentBrowseName, variableType, espBatteryCurrentAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes espBatterySocAttr = UA_VariableAttributes_default;
    
    espBatterySocAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatterySocAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatterySOC");
    UA_Double espBatterySOC = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatterySocAttr.value, &espBatterySOC, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatterySocNodeId = UA_NODEID_STRING(14, "esp.battery.SOC");
    UA_QualifiedName espBatterySocBrowseName = UA_QUALIFIEDNAME(14, "espBatterySOC");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatterySocNodeId, parentNodeId, parentReferenceNodeId,
                              espBatterySocBrowseName, variableType, espBatterySocAttr, NULL, NULL);
    
    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes espBatteryDischargeCurrentAttr = UA_VariableAttributes_default;
    
    espBatteryDischargeCurrentAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryDischargeCurrentAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryDischargeCurrent");
    UA_Double espBatteryDischargeCurrent = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryDischargeCurrentAttr.value, &espBatteryDischargeCurrent, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryDischargeCurrentNodeId = UA_NODEID_STRING(15, "esp.battery.dischargecurrent");
    UA_QualifiedName espBatteryDischargeCurrentBrowseName = UA_QUALIFIEDNAME(15, "espBatteryDischargeCurrent");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryDischargeCurrentNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryDischargeCurrentBrowseName, variableType, espBatteryDischargeCurrentAttr, NULL, NULL);
    
    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes espBatteryChargerVoltageAttr = UA_VariableAttributes_default;
    
    espBatteryChargerVoltageAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryChargerVoltageAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryChargerVoltage");
    UA_Double espBatteryChargerVoltage = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryChargerVoltageAttr.value, &espBatteryChargerVoltage, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryChargerVoltageNodeId = UA_NODEID_STRING(16, "esp.battery.chargervoltage");
    UA_QualifiedName espBatteryChargerVoltageBrowseName = UA_QUALIFIEDNAME(16, "espBatteryChargerVoltage");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryChargerVoltageNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryChargerVoltageBrowseName, variableType, espBatteryChargerVoltageAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes espBatteryChargerEnableAttr = UA_VariableAttributes_default;
    
    espBatteryChargerEnableAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryChargerEnableAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryChargerEnable");
    UA_Double espBatteryChargerEnable = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryChargerEnableAttr.value, &espBatteryChargerEnable, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryChargerEnableNodeId = UA_NODEID_STRING(17, "esp.battery.chargerenable");
    UA_QualifiedName espBatteryChargerEnableBrowseName = UA_QUALIFIEDNAME(17, "espBatteryChargerEnable");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryChargerEnableNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryChargerEnableBrowseName, variableType, espBatteryChargerEnableAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes espBatteryDischargerEnableAttr = UA_VariableAttributes_default;
    
    espBatteryDischargerEnableAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    espBatteryDischargerEnableAttr.displayName = UA_LOCALIZEDTEXT("en-US", "espBatteryDischargerEnable");
    UA_Double espBatteryDischargerEnable = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&espBatteryDischargerEnableAttr.value, &espBatteryDischargerEnable, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId espBatteryDischargerEnableNodeId = UA_NODEID_STRING(18, "esp.battery.dischargerenable");
    UA_QualifiedName espBatteryDischargerEnableBrowseName = UA_QUALIFIEDNAME(18, "espBatteryDischargerEnable");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, espBatteryDischargerEnableNodeId, parentNodeId, parentReferenceNodeId,
                              espBatteryDischargerEnableBrowseName, variableType, espBatteryDischargerEnableAttr, NULL, NULL);

    /*------------------------------------------------------------------------------------------*/

    UA_VariableAttributes simulationTimeAttr = UA_VariableAttributes_default;
    
    simulationTimeAttr.accessLevel = UA_ACCESSLEVELMASK_READ | UA_ACCESSLEVELMASK_WRITE;

    simulationTimeAttr.displayName = UA_LOCALIZEDTEXT("en-US", "simulationTime");
    UA_Double simulationTime = 0; // Valor de exemplo para a tensão da bateria
    UA_Variant_setScalar(&simulationTimeAttr.value, &simulationTime, &UA_TYPES[UA_TYPES_DOUBLE]);

    /* 2) Definir onde o nó será adicionado e qual o nome de navegação */
    UA_NodeId simulationTimeNodeId = UA_NODEID_STRING(19, "simulation.time");
    UA_QualifiedName simulationTimeBrowseName = UA_QUALIFIEDNAME(19, "simulationTime");

    /* 3) Adicionar o nó */
    UA_Server_addVariableNode(server, simulationTimeNodeId, parentNodeId, parentReferenceNodeId,
                              simulationTimeBrowseName, variableType, simulationTimeAttr, NULL, NULL);

    /* Executar o loop do servidor */
    UA_StatusCode status = UA_Server_run(server, &running);

    UA_Server_delete(server);
    return status;
}