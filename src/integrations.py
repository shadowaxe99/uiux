```python
class IDEIntegration:
    def __init__(self, ide_name, integration_details):
        self.ide_name = ide_name
        self.integration_details = integration_details

ideIntegrations = {}

def integrateIDE(ide_name, integration_details):
    global ideIntegrations
    ideIntegrations[ide_name] = IDEIntegration(ide_name, integration_details)

def getIntegration(ide_name):
    global ideIntegrations
    return ideIntegrations.get(ide_name, None)

def updateIntegration(ide_name, new_integration_details):
    global ideIntegrations
    if ide_name in ideIntegrations:
        ideIntegrations[ide_name].integration_details = new_integration_details

def removeIntegration(ide_name):
    global ideIntegrations
    if ide_name in ideIntegrations:
        del ideIntegrations[ide_name]
```