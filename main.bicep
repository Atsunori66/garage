targetScope = 'subscription'

param rgName string = 'rg2-bicep'
param location string = 'japaneast'
param strName string = 'noristrbicep2'

resource rg1 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: rgName
  location: location
}

module str1 './modules/storage.bicep' = {
  name: 'storageModule'
  scope: rg1
  params: {
    storageName: strName
    storageLocation: location
  }
}
