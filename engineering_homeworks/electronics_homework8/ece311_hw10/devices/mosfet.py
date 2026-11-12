import math
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
        
        self.polarity = polarity
        self.v_threshold = self.parameter_validation("Threshold voltage", v_threshold)
        self.k = self.parameter_validation("Transconductance parameter", k)
        self.clm = self.parameter_validation("Channel lenght modulation", clm)
        
        if self.v_threshold <= 0:
            raise ValueError("Input magnitude of threshold voltage")
        
        if self.k <= 0:
            raise ValueError("Input must be greater then zero")
        
        if self.clm < 0:
            raise ValueError("CLM cannot be negative")
    
    @staticmethod
    def parameter_validation(name, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be numeric")
        
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")
        
        return value
        
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
            return self.k * (2 * v_ov * v_ds - v_ds ** 2) * (1 + self.clm * v_ds)
        
        if region == "Saturation": 
            return self.k * v_ov ** 2 * (1 + self.clm * v_ds)
        
        raise ValueError("Unsupported operating region")   
    
    def calculate_transconductance(self, v_g, v_d, v_s):
        region = self.check_region(v_g, v_d, v_s)
        
        if region == "Cutoff":
            return 0.0
        
        v_ov = self.calculate_overdrive_voltage(v_g, v_s)
        v_ds = self.calculate_effective_vds(v_d, v_s)
        
        if region == "Triode":
            return 2 * self.k * v_ds * (1 + self.clm * v_ds)
        
        if region == "Saturation":
            return 2 * self.k * v_ov * (1 + self.clm * v_ds)
        
        raise ValueError("Unsupported operating region")   
        
    def calculate_output_resistance(self, v_g, v_d, v_s):
        region = self.check_region(v_g, v_d, v_s)
        
        if region == "Cutoff":
            return float('inf')
        
        if region == "Triode":
            raise ValueError("Output resistance calculation only supported in saturation")
        
        if self.clm == 0:
            return float('inf')
        
        v_ov = self.calculate_overdrive_voltage(v_g, v_s)
        
        return 1 / (self.clm * self.k * v_ov ** 2)
        