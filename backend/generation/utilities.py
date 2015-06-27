__author__ = 'm5z'


def output_utilities():
    utilities = [
        [u"FuelFactors", u"Electricity", u"kg", u"", u"3.546", u"", u"3.417E+02", u"", u"1.186E-01", u"", u"7.472E-01",
         u"", u"6.222E-01", u"", u"8.028E-03", u"", u"1.872E+00", u"", u"0.0", u"", u"1.739E-02", u"", u"0.0", u"",
         u"0.0", u"", u"1.019E-02", u"", u"5.639E-06", u"", u"2.778E-05", u"", u"0.4309556", u"", u"0", u"", u"0"],
        [u"FuelFactors", u"NaturalGas", u"m3", u"37631000", u"1.092", u"", u"5.21E+01", u"", u"3.99E-02", u"",
         u"1.06E-03", u"", u"4.73E-02", u"", u"1.06E-03", u"", u"2.68E-04", u"", u"0.0", u"", u"3.59E-03", u"", u"0.0",
         u"", u"0", u"", u"2.61E-03", u"", u"1.11E-07", u"", u"2.13E-07", u"", u"0", u"", u"0", u"", u"0"],
        [u"UtilityCost:Tariff", u"PSI_LLF_LowLoadFactorService", u"Electricity:Facility", u"kWh", u"", u"", u"", u"",
         u"", u"HalfHour", u"15.00", u"", u"", u"", u"Comm Elect"],
        [u"UtilityCost:Charge:Block", u"AnnualEnergyCharge", u"PSI_LLF_LowLoadFactorService", u"totalEnergy", u"Annual",
         u"EnergyCharges", u"", u"", u"300", u"0.108222", u"700", u"0.087021", u"1500", u"0.078420", u"remaining",
         u"0.058320"],
        [u"UtilityCost:Charge:Block", u"AnnualDemandBaseCharge", u"PSI_LLF_LowLoadFactorService", u"totalEnergy",
         u"Annual", u"EnergyCharges", u"", u"TotalDemand", u"190", u"0.0", u"110", u"0.051773", u"remaining",
         u"0.046965"],
        [u"UtilityCost:Charge:Simple", u"FuelCostAdjustEnergyCharge", u"PSI_LLF_LowLoadFactorService", u"totalEnergy",
         u"Annual", u"EnergyCharges", u"0.002028"],
        [u"UtilityCost:Charge:Simple", u"QualPollutionControlAdjustEnergyCharge", u"PSI_LLF_LowLoadFactorService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.000536"],
        [u"UtilityCost:Charge:Simple", u"SoxNoxRiderAdjustEnergyCharge", u"PSI_LLF_LowLoadFactorService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.001127"],
        [u"UtilityCost:Charge:Simple", u"DSMRiderAdjustEnergyCharge", u"PSI_LLF_LowLoadFactorService", u"totalEnergy",
         u"Annual", u"EnergyCharges", u"-0.000370"],
        [u"UtilityCost:Charge:Simple", u"PurchPowerTrackerAdjustEnergyCharge", u"PSI_LLF_LowLoadFactorService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"-0.000031"],
        [u"UtilityCost:Charge:Simple", u"MidwestISOAdjustEnergyCharge", u"PSI_LLF_LowLoadFactorService", u"totalEnergy",
         u"Annual", u"EnergyCharges", u"-0.000216"],
        [u"UtilityCost:Charge:Simple", u"CleanCoalRiderEnergyCharge", u"PSI_LLF_LowLoadFactorService", u"totalEnergy",
         u"Annual", u"EnergyCharges", u"0.000833"],
        [u"UtilityCost:Qualify", u"MinDemand75kw", u"PSI_LLF_LowLoadFactorService", u"TotalDemand", u"Minimum", u"75",
         u"Annual", u"Count", u"12"],
        [u"UtilityCost:Charge:Simple", u"TaxofeightPercent", u"PSI_LLF_LowLoadFactorService", u"SubTotal", u"Annual",
         u"Taxes", u"0.08"],
        [u"UtilityCost:Tariff", u"PSI_CS_CommercialElectricService", u"Electricity:Facility", u"kWh", u"", u"", u"",
         u"", u"", u"", u"9.40", u"", u"", u"", u"Comm Elect"],
        [u"UtilityCost:Charge:Block", u"AnnualEnergyCharge", u"PSI_CS_CommercialElectricService", u"totalEnergy",
         u"Annual", u"EnergyCharges", u"", u"", u"300", u"0.082409", u"700", u"0.072873", u"1500", u"0.061696",
         u"remaining", u"0.041179"],
        [u"UtilityCost:Charge:Simple", u"FuelCostAdjustEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.002028"],
        [u"UtilityCost:Charge:Simple", u"QualPollutionControlAdjustEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.000536"],
        [u"UtilityCost:Charge:Simple", u"SoxNoxRiderAdjustEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.001127"],
        [u"UtilityCost:Charge:Simple", u"DSMRiderAdjustEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.000021"],
        [u"UtilityCost:Charge:Simple", u"PurchPowerTrackerAdjustEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.000034"],
        [u"UtilityCost:Charge:Simple", u"MidwestISOAdjustEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"-0.000203"],
        [u"UtilityCost:Charge:Simple", u"CleanCoalRiderEnergyCharge", u"PSI_CS_CommercialElectricService",
         u"totalEnergy", u"Annual", u"EnergyCharges", u"0.000807"],
        [u"UtilityCost:Qualify", u"MaxDemand75kw", u"PSI_CS_CommercialElectricService", u"TotalDemand", u"Maximum",
         u"75", u"Annual", u"Count", u"1"],
        [u"UtilityCost:Charge:Simple", u"TaxofeightPercent", u"PSI_CS_CommercialElectricService", u"SubTotal",
         u"Annual", u"Taxes", u"0.08"],
        [u"UtilityCost:Tariff", u"IN_EIAMonthlyRateGas", u"Gas:Facility", u"MCF", u"", u"", u"", u"", u"", u"", u"0.0",
         u"", u"", u"", u"Comm Gas"],
        [u"UtilityCost:Charge:Simple", u"MonthlyRateGasCharge", u"IN_EIAMonthlyRateGas", u"totalEnergy", u"Annual",
         u"EnergyCharges", u"IN_MonthlyGasRates"],
        [u"UtilityCost:Variable", u"IN_MonthlyGasRates", u"IN_EIAMonthlyRateGas", u"Currency", u"8.22", u"7.51",
         u"8.97", u"9.01", u"9.16", u"10.44", u"10.32", u"10.13", u"9.20", u"8.18", u"7.83", u"7.63"],
        [u"UtilityCost:Charge:Simple", u"TaxofEightPercent", u"IN_EIAMonthlyRateGas", u"SubTotal", u"Annual", u"Taxes",
         u"0.08"]]
    return utilities