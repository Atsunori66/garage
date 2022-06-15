param storageName string
param storageLocation string

resource storageaccount 'Microsoft.Storage/storageAccounts@2021-09-01' = {
  name: storageName
  location: storageLocation
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    isHnsEnabled: true
  }
}
