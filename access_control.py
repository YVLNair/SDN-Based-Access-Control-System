from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# Whitelist MACs (Mininet --mac required)
ALLOWED_MACS = [
    "00:00:00:00:00:01",  # h1
    "00:00:00:00:00:02"   # h2
]

def _handle_PacketIn(event):
    packet = event.parsed
    src = str(packet.src)

    if src in ALLOWED_MACS:
        log.info(f"[ALLOWED] {src}")

        msg = of.ofp_flow_mod()
        msg.match.dl_src = packet.src
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

        event.connection.send(msg)
    else:
        log.info(f"[BLOCKED] {src}")
        # No action = dropped

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("SDN Access Control Started")
