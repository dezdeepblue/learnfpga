target = "xilinx"
action = "synthesis"

syn_device = "xc6slx25"
syn_grade = "-3"
syn_package = "ftg256"
syn_top = "midi2"
syn_project = "midi2.xise"
syn_tool = "ise"

modules = {
    "local" : [ "../vhdl" ],
}


