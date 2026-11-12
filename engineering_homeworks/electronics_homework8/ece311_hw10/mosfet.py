class MOSFET:
    def __init__(self, device_type, v_threshold, k, clm = 0.0):
        if not isinstance(device_type, str):
            raise TypeError("Input NMOS or PMOS")
        if device_type.upper().strip() not in ("NMOS", "PMOS"):
            raise ValueError("Input NMOS or PMOS")
        self.device_type = device_type.strip().upper()
        
        if self.device_type == "NMOS":
            polarity = 1
        else:
            polarity = -1
        
        if not isinstance(v_threshold, (int, float)):
            raise TypeError("Input voltage value")
        if v_threshold <= 0:
            raise ValueError("Input magnitude of threshold voltage")
        
        if not isinstance(k, (int, float)):
            raise TypeError("Input a numeric value")
        if k <= 0:
            raise ValueError("Input must be greater then zero")
        
        if not isinstance(clm, (int, float)):
            raise TypeError("Input a numeric value")
        if clm < 0:
            raise ValueError("CLM cannot be negative")
        
        self.polarity = polarity
        self.v_threshold = v_threshold
        self.k = k
        self.clm = clm
        
    def calculate_overdrive_voltage(self, v_g, v_s):
        v_gs = v_g - v_s
        v_ov = self.polarity * v_gs - self.v_threshold
        return v_ov
    
    def calculate_effective_vds(self, v_d, v_s):
        v_ds_eff = self.polarity * (v_d - v_s)
        return v_ds_eff
    
    def check_region(self, v_g, v_d, v_s):
        v_ov = self.calculate_overdrive_voltage(v_g, v_s)
        v_ds = self.calculate_effective_vds(v_d, v_s)
        
        if v_ov <= 0:
            return "Cutoff"
        
        if v_ds < 0:
            raise ValueError("Reverse operation not supported")
        
        if v_ds < v_ov:
            return "Triode"
        
        return "Saturation"
    
    def calculate_drain_current(self, v_g, v_d, v_s):
        region = self.check_region(v_g, v_d, v_s)
        
        if region == "Cutoff":
            return 0.0
        
        v_ov = self.calculate_overdrive_voltage(v_g, v_s)
        v_ds = self.calculate_effective_vds(v_d, v_s)
        
        if region == "Triode":
            return self.k * (2 * v_ov * v_ds - v_ds ** 2)
        
        if region == "Saturation": 
            return self.k * v_ov ** 2
        
        raise ValueError("Unsupported operating region")
    
    def calculate_transconductance(self, v_g, v_s):
        v_ov = self.calculate_overdrive_voltage(v_g, v_s)
        return 2 * self.k * v_ov