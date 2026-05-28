from typing import Dict, Any

class TaxSimulation:
    """
    Simulates changes in actual Spanish tax regulations.
    Incorporates real Spanish tax frameworks:
    - IVA (Impuesto sobre el Valor Añadido): General 21%, Reducido 10%, Superreducido 4%
    - IRPF (Impuesto sobre la Renta de las Personas Físicas)
    - Impuesto de Sociedades (Corporate Tax for S.L.s - General rate 25%, reduced for startups 15%)
    """
    
    @staticmethod
    def generate_iva_reform(
        new_general_rate: float = 23.0, 
        new_reducido_rate: float = 12.0,
        effective_date: str = "2026-07-01",
        affected_sectors: list = ["retail", "clothing"]
    ) -> Dict[str, Any]:
        """
        Simulates an adjustment to Spanish IVA brackets.
        """
        return {
            "scenario_type": "tax_reform_iva",
            "description": f"BOE simulation: The Spanish Government raises General IVA to {new_general_rate}% and Reducido to {new_reducido_rate}% effective {effective_date}.",
            "tax_details": {
                "general_iva_rate": new_general_rate,
                "reducido_iva_rate": new_reducido_rate,
            },
            "effective_date": effective_date,
            "affected_sectors": affected_sectors,
            "required_actions": ["Update invoicing systems", "Calculate margin compression", "Generate Modelo 303 impact report"]
        }

    @staticmethod
    def generate_sociedades_reform(
        new_corporate_rate: float = 28.0,
        effective_date: str = "2027-01-01"
    ) -> Dict[str, Any]:
        """
        Simulates an adjustment to the Spanish Corporate Tax (Impuesto de Sociedades).
        """
        return {
            "scenario_type": "tax_reform_sociedades",
            "description": f"BOE simulation: Corporate tax rate for S.L. entities increased from 25% to {new_corporate_rate}%.",
            "tax_details": {
                "impuesto_sociedades_rate": new_corporate_rate,
                "modelo_200_impact": True
            },
            "effective_date": effective_date,
            "required_actions": ["Calculate net profit reduction", "Adjust dividend strategy", "Generate Modelo 200 forecast"]
        }
