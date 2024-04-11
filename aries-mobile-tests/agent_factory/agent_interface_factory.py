"""
Factory class to create agent interface objects 
given the agent type passed in.
"""
from agent_factory.aath.aath_issuer_agent_interface import \
    AATHIssuerAgentInterface
from agent_factory.aath.aath_verifier_agent_interface import \
    AATHVerifierAgentInterface
from agent_factory.bc_person_showcase.bc_person_showcase_verifier_agent_interface import \
    BCPersonShowcaseVerifierAgentInterface
from agent_factory.bc_showcase.bc_showcase_issuer_agent_interface import \
    BCShowcaseIssuerAgentInterface
from agent_factory.bc_showcase.bc_showcase_verifier_agent_interface import \
    BCShowcaseVerifierAgentInterface
from agent_factory.bc_vp.bc_vp_issuer_agent_interface import \
    BC_VP_IssuerAgentInterface
from agent_factory.candy_uvp.candy_uvp_issuer_agent_interface import \
    CANdy_UVP_IssuerAgentInterface
from agent_factory.issuer_agent_interface import IssuerAgentInterface
from agent_factory.mcn.mcn_issuer_agent_interface import \
    MCNIssuerAgentInterface
from agent_factory.mcn.mcn_verifier_agent_interface import \
    MCNVerifierAgentInterface
from agent_factory.verifier_agent_interface import VerifierAgentInterface


class AgentInterfaceFactory:
    issuer_agent_type_interface_dict = {
        "AATH": AATHIssuerAgentInterface,
        "MCN": MCNIssuerAgentInterface,
        "CANdy_UVP": CANdy_UVP_IssuerAgentInterface,
        "BC_VP": BC_VP_IssuerAgentInterface,
        "BCShowcaseIssuer": BCShowcaseIssuerAgentInterface,
    }
    verifier_agent_type_interface_dict = {
        "AATH": AATHVerifierAgentInterface,
        "MCN": MCNVerifierAgentInterface,
        "BC_Person_Showcase": BCPersonShowcaseVerifierAgentInterface,
        "BCShowcaseVerifier": BCShowcaseVerifierAgentInterface,
    }

    def create_issuer_agent_interface(
        self, agent_type, agent_endpoint
    ) -> IssuerAgentInterface:
        """create an issuer agent interface object of the type given"""
        return self.issuer_agent_type_interface_dict[agent_type](agent_endpoint)

    def create_verifier_agent_interface(
        self, agent_type, agent_endpoint
    ) -> VerifierAgentInterface:
        """create a verifier agent interface object of the type given"""
        return self.verifier_agent_type_interface_dict[agent_type](agent_endpoint)
