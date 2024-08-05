
def get_base_64():
    return """
aW1wb3J0IGFnZW50CmltcG9ydCB2ZWN0b3JhZ2VudAoKaW1wb3J0IG9zCmZyb20gZmxhc2sgaW1w
b3J0IEZsYXNrLHJlcXVlc3QsanNvbmlmeQppbXBvcnQgeWFtbAoKYXBwID0gRmxhc2soX19uYW1l
X18pCgojIGZpcnN0IHVzZSBzZWN0aW9uCgpAYXBwLnJvdXRlKCIvIikKZGVmIHdlbGNvbWVfYmFj
a19lbmQoKToKICAgIHJldHVybiAiPGgxPldlbGNvbWUgdG8gc2ltcGxlIGNyZXcgYWk8L2gxPiIK
CkBhcHAucm91dGUoIi90YXNrIixtZXRob2RzPVsnUE9TVCddKQpkZWYgYWdlbnRzKCk6CgogICAg
ICAgIGpzb25fZGF0YSA9IHJlcXVlc3QuanNvbgogICAgICAgIG5hbWVfYWdlbnQgPSBqc29uX2Rh
dGEuZ2V0KCduYW1lJykKICAgICAgICB0YXNrc19hZ2VudCA9IGpzb25fZGF0YS5nZXQoJ3Rhc2tz
JykKICAgICAgICB3ZWJfYWdlbnQgPSBqc29uX2RhdGEuZ2V0KCd3ZWInKQogICAgICAgIG1vZGVs
X2FnZW50ID0ganNvbl9kYXRhLmdldCgnbW9kZWwnKQogICAgICAgIHJlc3RfYWdlbnQgPSBhZ2Vu
dC5hZ2VudChuYW1lPW5hbWVfYWdlbnQsdGFza3M9dGFza3NfYWdlbnQsd2ViPXdlYl9hZ2VudCxt
b2RlbD1tb2RlbF9hZ2VudCkKICAgICAgICAgIAogICAgICAgIG91dHB1dCA9IHsicmVzcG9uc2Ui
OnJlc3RfYWdlbnQuZG9UYXNrKCl9ICAgCiAgICAgICAgcmV0dXJuIGpzb25pZnkob3V0cHV0KQoK
IyB2ZWN0b3Igc2VjdGlvbgoKQGFwcC5yb3V0ZSgiL3ZlY3RvciIsbWV0aG9kcz1bJ1BPU1QnXSkK
ZGVmIHZlY3RvcmRiKCk6CiAgICBqc29uX2RhdGEgPSByZXF1ZXN0Lmpzb24KICAgIGNvbGxlY3Rp
b24gPSBqc29uX2RhdGEuZ2V0KCdjb2xsZWN0aW9uJykKICAgIHZlY3Rvcl9kYXRhID0ganNvbl9k
YXRhLmdldCgncHJvbXB0JykKICAgIHRvcGljID0ganNvbl9kYXRhLmdldCgndG9waWMnKQogICAg
dG9waWNfaWQgPSBqc29uX2RhdGEuZ2V0KCd0b3BpY19pZCcpCgogICAgdmVjdG9yX2FnZW50ID0g
dmVjdG9yYWdlbnQudmVjdG9yQWdlbnQobmFtZV9jb2xsZWN0aW9uPWNvbGxlY3Rpb24sZGF0YV9w
dXQ9dmVjdG9yX2RhdGEsdG9waWM9dG9waWMsdG9waWNfaWQ9dG9waWNfaWQpCiAgICByZXR1cm4g
dmVjdG9yX2FnZW50LmRvVmVjdG9yKCkKCkBhcHAucm91dGUoIi9yZXRyaWV2ZXZlY3RvciIsbWV0
aG9kcz1bJ1BPU1QnXSkKZGVmIGxvY2FsdmVjdG9yKCk6IAogICAganNvbl9kYXRhID0gcmVxdWVz
dC5qc29uCiAgICBjb2xsZWN0aW9uID0ganNvbl9kYXRhLmdldCgnY29sbGVjdGlvbicpCiAgICB0
b3BpY19kYXRhID0ganNvbl9kYXRhLmdldCgndG9waWMnKQogICAgdmVjdG9yX2RhdGEgPSBqc29u
X2RhdGEuZ2V0KCdwcm9tcHQnKQoKICAgIHZlY3Rvcl9hZ2VudCA9IHZlY3RvcmFnZW50LnZlY3Rv
ckFnZW50KG5hbWVfY29sbGVjdGlvbj1jb2xsZWN0aW9uLGRhdGFfcHV0PXZlY3Rvcl9kYXRhLHRv
cGljPXRvcGljX2RhdGEsdG9waWNfaWQ9Tm9uZSkKICAgIHJldHVybiB2ZWN0b3JfYWdlbnQuZ2V0
VmVjdG9yKCkKCkBhcHAucm91dGUoIi9kZWxldGV2ZWN0b3IiLG1ldGhvZHM9WydQT1NUJ10pCmRl
ZiByZW1vdmVfdmVjdG9yX2RhdGEoKToKICAgIGpzb25fZGF0YSA9IHJlcXVlc3QuanNvbgogICAg
Y29sbGVjdGlvbiA9IGpzb25fZGF0YS5nZXQoJ2NvbGxlY3Rpb24nKQogICAgcXVlcnkgPSBqc29u
X2RhdGEuZ2V0KCdxdWVyeScpCgogICAgaWYgcXVlcnkgaXMgTm9uZToKICAgICAgICBvcGVyYXRp
b24gPSB7Im9wZXJhdGlvbiI6Im5vdCBjb25jbHVkZWQiLCJlcnJvciI6IlRoZSBxdWVyeSBwYXNz
ZWQgaGFzIG5vIHZhbHVlIn0KICAgICAgICByZXR1cm4ganNvbmlmeShvcGVyYXRpb24pCgogICAg
dmVjdG9yX2FnZW50ID0gdmVjdG9yYWdlbnQudmVjdG9yQWdlbnQobmFtZV9jb2xsZWN0aW9uPWNv
bGxlY3Rpb24sZGF0YV9wdXQ9Tm9uZSx0b3BpYz1Ob25lLHRvcGljX2lkPU5vbmUpCiAgICByZXR1
cm4gdmVjdG9yX2FnZW50LnJlbW92ZVZlY3RvcihxdWVyeSkKCkBhcHAucm91dGUoIi9kZWxldGVj
b2xsZWN0aW9uIixtZXRob2RzPVsnUE9TVCddKQpkZWYgcmVtb3ZlX2NvbGxlY3Rpb24oKToKICAg
IGpzb25fZGF0YSA9IHJlcXVlc3QuanNvbgogICAgY29sbGVjdGlvbiA9IGpzb25fZGF0YS5nZXQo
J2NvbGxlY3Rpb24nKQoKICAgIGlmIGNvbGxlY3Rpb24gaXMgTm9uZToKICAgICAgICBvcGVyYXRp
b24gPSB7Im9wZXJhdGlvbiI6Im5vdCBjb25jbHVkZWQiLCJlcnJvciI6IlRoZSBxdWVyeSBwYXNz
ZWQgaGFzIG5vIHZhbHVlIn0KICAgICAgICByZXR1cm4ganNvbmlmeShvcGVyYXRpb24pICAgICAg
ICAKCiAgICB2ZWN0b3JfYWdlbnQgPSB2ZWN0b3JhZ2VudC52ZWN0b3JBZ2VudChuYW1lX2NvbGxl
Y3Rpb249Y29sbGVjdGlvbixkYXRhX3B1dD1Ob25lLHRvcGljPU5vbmUsdG9waWNfaWQ9Tm9uZSkK
ICAgIHJldHVybiB2ZWN0b3JfYWdlbnQucmVtb3ZlQ29sbGVjdGlvbigpCgoKQGFwcC5yb3V0ZSgi
L3BvcHVsYXRld2VidmVjdG9yIixtZXRob2RzPVsnUE9TVCddKQpkZWYgcG9wdWxhdGVfd2ViX3Zl
Y3RvcigpOgogICAganNvbl9kYXRhID0gcmVxdWVzdC5qc29uCiAgICBjb2xsZWN0aW9uID0ganNv
bl9kYXRhLmdldCgnY29sbGVjdGlvbicpCiAgICBzZWFyY2hfdGVybSA9IGpzb25fZGF0YS5nZXQo
J3F1ZXJ5JykKCiAgICB2ZWN0b3JfYWdlbnQgPSB2ZWN0b3JhZ2VudC52ZWN0b3JBZ2VudChuYW1l
X2NvbGxlY3Rpb249Y29sbGVjdGlvbixkYXRhX3B1dD1Ob25lLHRvcGljPU5vbmUsdG9waWNfaWQ9
Tm9uZSkKICAgIHJldHVybiB2ZWN0b3JfYWdlbnQucG9wdWxhdGVXZWJWZWN0b3Ioc2VhcmNoX3Rl
cm0pIAoKQGFwcC5yb3V0ZSgiL3VwZGF0ZXZlY3RvciIsbWV0aG9kcz1bJ1BPU1QnXSkKZGVmIHVw
ZGF0ZV92ZWN0b3IoKToKICAgIGpzb25fZGF0YSA9IHJlcXVlc3QuanNvbgogICAgY29sbGVjdGlv
biA9IGpzb25fZGF0YS5nZXQoJ2NvbGxlY3Rpb24nKQogICAgdmVjdG9yX2RhdGEgPSBqc29uX2Rh
dGEuZ2V0KCdwcm9tcHQnKQogICAgdG9waWMgPSBqc29uX2RhdGEuZ2V0KCd0b3BpYycpCiAgICB0
b3BpY19pZCA9IGpzb25fZGF0YS5nZXQoJ3RvcGljX2lkJykKCiAgICB2ZWN0b3JfYWdlbnQgPSB2
ZWN0b3JhZ2VudC52ZWN0b3JBZ2VudChuYW1lX2NvbGxlY3Rpb249Y29sbGVjdGlvbixkYXRhX3B1
dD12ZWN0b3JfZGF0YSx0b3BpYz10b3BpYyx0b3BpY19pZD10b3BpY19pZCkKICAgIHJldHVybiB2
ZWN0b3JfYWdlbnQudXBkYXRlVmVjdG9yKCkKCiMgdHJhaW4gc2VjdGlvbgoKQGFwcC5yb3V0ZSgi
L3RyYWludmVjdG9yIixtZXRob2RzPVsnUE9TVCddKQpkZWYgdHJhaW5fd2l0aF92ZWN0b3IoKToK
ICAgIGpzb25fZGF0YSA9IHJlcXVlc3QuanNvbgogICAgbW9kZWwgPSBqc29uX2RhdGEuZ2V0KCdt
b2RlbCcpCiAgICBxdWVyeSA9IGpzb25fZGF0YS5nZXQoJ3F1ZXJ5JykKICAgIGNvbGxlY3Rpb24g
PSBqc29uX2RhdGEuZ2V0KCdjb2xsZWN0aW9uJykKCiAgICB2ZWN0b3JfYWdlbnQgPSB2ZWN0b3Jh
Z2VudC52ZWN0b3JBZ2VudChuYW1lX2NvbGxlY3Rpb249Y29sbGVjdGlvbixkYXRhX3B1dD1Ob25l
LHRvcGljPU5vbmUsdG9waWNfaWQ9Tm9uZSkKICAgIHZlY3Rvcl9hZ2VudC50cmFpbkxMTShxdWVy
eSxtb2RlbCkKCiAgICByZXR1cm4gdmVjdG9yX2FnZW50LnRyYWluTExNKHF1ZXJ5LG1vZGVsKQoK
CmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CiAgICBhcHAucnVuKHBvcnQ9e1BPUlR9KQogICAg
CgoK
"""

def put_agent():
    return """
aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCBkdWNrZHVja2dvX3NlYXJjaAoKaW1w
b3J0IHZlY3Rvcm1hbmFnZXIKCmZyb20gZmxhc2sgaW1wb3J0IGpzb25pZnkKCgpjbGFzcyBhZ2Vu
dDoKCiAgICBkZWYgX19pbml0X18oc2VsZiwgbmFtZSx0YXNrcyx3ZWIsbW9kZWwpOgogICAgICAg
IHNlbGYuX19uYW1lID0gbmFtZQogICAgICAgIHNlbGYuX190YXNrcyA9IHRhc2tzCiAgICAgICAg
c2VsZi5fX3dlYiA9IHdlYgogICAgICAgIHNlbGYuX19tb2RlbCA9IG1vZGVsCgogICAgZGVmIGdl
dE5hbWUoc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYuX19uYW1lCgogICAgZGVmIHNldE5hbWUo
c2VsZixuYW1lKToKICAgICAgICBzZWxmLl9fbmFtZSA9IG5hbWUgICAKCiAgICBkZWYgZ2V0VGFz
a3Moc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYuX190YXNrczsKCiAgICBkZWYgc2V0VGFza3Mo
c2VsZix0YXNrdik6CiAgICAgICAgc2VsZi5fX3Rhc2tzID0gdGFza3YKCiAgICBkZWYgZ2V0V2Vi
KHNlbGYpOgogICAgICAgIHJldHVybiBzZWxmLl9fd2ViICAgICAKCiAgICBkZWYgc2V0V2ViKHNl
bGYsd2VieCk6CiAgICAgICAgc2VsZi5fX3dlYiA9IHdlYngKCiAgICBkZWYgZ2V0TW9kZWwoc2Vs
Zik6CiAgICAgICAgcmV0dXJuIHNlbGYuX19tb2RlbAoKICAgIGRlZiBzZXRNb2RlbChzZWxmLG1v
ZGVseCk6CiAgICAgICAgc2VsZi5fX21vZGVsID0gbW9kZWx4ICAgICAgICAgICAgICAgCgogICAg
CiAgICBkZWYgZG9UYXNrKHNlbGYpOgogICAgICAgIHByaW50KCJGb2xsb3dpbmcgYWdlbnQgaXMg
cnVubmluZzoiKQogICAgICAgIHByaW50KHNlbGYuX19uYW1lKQogICAgICAgIAoKICAgICAgICBm
b3IgdGFzayBpbiBzZWxmLl9fdGFza3M6CiAgICAgICAgICAgIAogICAgICAgICAgICBwcmludCgi
cHJvbXB0aW5nIHRoZSBmb2xsb3dpbmcgdGFzazogIikKICAgICAgICAgICAgcHJpbnQodGFzaykK
CiAgICAgICAgICAgIGRhdGEgPSB7J21vZGVsJzpzZWxmLl9fbW9kZWwsJ3Byb21wdCc6dGFzaywn
c3RyZWFtJzpGYWxzZX0KCiAgICAgICAgICAgIGlmIHNlbGYuX193ZWIgaXMgVHJ1ZToKCiAgICAg
ICAgICAgICAgICByZXNlYXJjaF93ZWIgPSB0YXNrCiAgICAgICAgICAgICAgICBkdWNrX2R1Y2tf
c2VhcmNoID0gZHVja2R1Y2tnb19zZWFyY2guRERHUygpLnRleHQocmVzZWFyY2hfd2ViLG1heF9y
ZXN1bHRzPTUpCiAgICAgICAgICAgICAgICBtYXRlcmlhbF90b19sZWFybiA9IFtdCgogICAgICAg
ICAgICAgICAgcHJpbnQoInJldHJpZXZpbmcgZnJvbSB0aGUgd2ViIikKICAgICAgICAgICAgICAg
IGZvciBzZWFyY2hfcmVzdWx0cyBpbiBkdWNrX2R1Y2tfc2VhcmNoOgogICAgICAgICAgICAgICAg
ICAgIG1hdGVyaWFsX3RvX2xlYXJuLmFwcGVuZChzZWFyY2hfcmVzdWx0c1siYm9keSJdKQogICAg
ICAgICAgICAgICAgICAgIHByaW50KHNlYXJjaF9yZXN1bHRzWyJib2R5Il0pCiAgICAgICAgICAg
ICAgIAogICAgICAgICAgICAgICAgcHJpbnQoImxlYXJuaW5nIGZyb20gdGhlIHdlYiIpCgogICAg
ICAgICAgICAgICAgZm9yIGxlYXJuaW5nX2l0ZW0gaW4gbWF0ZXJpYWxfdG9fbGVhcm46CiAgICAg
ICAgICAgICAgICAgICAga25vd2xlZGdlX2RhdGEgPSB7Im1vZGVsIjpzZWxmLl9fbW9kZWwsInBy
b21wdCI6bGVhcm5pbmdfaXRlbX0gICAgCiAgICAgICAgICAgICAgICAgICAgZW1iZWRkaW5nX2Rh
dGEgPSByZXF1ZXN0cy5wb3N0KCJodHRwOi8vbG9jYWxob3N0OjExNDM0L2FwaS9lbWJlZGRpbmdz
Iixqc29uPWtub3dsZWRnZV9kYXRhKQoKICAgICAgICAgICAgICAgIHByaW50KCJhc2tpbmcgdG8g
dGhlIGxsbSIpCiAgICAgICAgICAgICAgICBwb3N0RGF0YSA9IHJlcXVlc3RzLnBvc3QoImh0dHA6
Ly9sb2NhbGhvc3Q6MTE0MzQvYXBpL2dlbmVyYXRlIixqc29uPWRhdGEpCiAgICAgICAgICAgICAg
ICBwcmludChwb3N0RGF0YS50ZXh0KQogICAgICAgICAgICAKICAgICAgICAgICAgZWxzZToKICAg
ICAgICAgICAgCiAgICAgICAgICAgICAgICBwb3N0RGF0YSA9IHJlcXVlc3RzLnBvc3QoImh0dHA6
Ly9sb2NhbGhvc3Q6MTE0MzQvYXBpL2dlbmVyYXRlIixqc29uPWRhdGEpCiAgICAgICAgICAgICAg
ICBwcmludChwb3N0RGF0YS50ZXh0KQogICAgICAgICAgICAKICAgICAgICAgICAgcmV0dXJuIHBv
c3REYXRhLmpzb24oKVsncmVzcG9uc2UnXQoK
"""

def vectormanager():
    return """
aW1wb3J0IGNocm9tYWRiCmltcG9ydCBjaHJvbWFkYi5hcGkKCgppbXBvcnQgcmVxdWVzdHMKZnJv
bSBmbGFzayBpbXBvcnQganNvbmlmeQoKZnJvbSBjaHJvbWFkYiBpbXBvcnQgU2V0dGluZ3MKCmlt
cG9ydCBkdWNrZHVja2dvX3NlYXJjaAoKY2xhc3MgdmVjdG9yTWFuYWdlcjoKCiAgICBkZWYgX19p
bml0X18oc2VsZixjb2xsZWN0aW9uKToKICAgICAgICAKICAgICAgICBzZWxmLl9fY29sbGVjdGlv
biA9IGNvbGxlY3Rpb24KICAgICAgICBzZWxmLl9fY2xpZW50ID0gY2hyb21hZGIuUGVyc2lzdGVu
dENsaWVudChwYXRoPSJwZXJzaXN0ZW50LmJsayIsc2V0dGluZ3M9U2V0dGluZ3MoYW5vbnltaXpl
ZF90ZWxlbWV0cnk9RmFsc2UpKQoKICAgIGRlZiBhZGRfb3JfY3JlYXRlX2RhdGEoc2VsZixkYXRh
LHRvcGljLHRvcGljX2lkKToKCiAgICAgICAgY29sbGVjdGlvbiA9IHNlbGYuX19jbGllbnQuZ2V0
X29yX2NyZWF0ZV9jb2xsZWN0aW9uKG5hbWU9c2VsZi5fX2NvbGxlY3Rpb24pCiAgICAgICAgY29s
bGVjdGlvbi5hZGQoZG9jdW1lbnRzID0gZGF0YSxtZXRhZGF0YXM9IHRvcGljLGlkcz0gdG9waWNf
aWQpCgogICAgICAgIG9wZXJhdGlvbiA9IHsib3BlcmF0aW9uIjoiY29uY2x1ZGVkIn0KICAgICAg
ICByZXR1cm4ganNvbmlmeShvcGVyYXRpb24pCgogICAgZGVmIGdpdmVfZGF0YShzZWxmLHRvcGlj
LHF1ZXJ5KToKCiAgICAgICAgY29sbGVjdGlvbiA9IHNlbGYuX19jbGllbnQuZ2V0X29yX2NyZWF0
ZV9jb2xsZWN0aW9uKG5hbWU9c2VsZi5fX2NvbGxlY3Rpb24pCiAgICAgICAgcmVzdWx0ID0gY29s
bGVjdGlvbi5xdWVyeShxdWVyeV90ZXh0cz0gcXVlcnksd2hlcmVfZG9jdW1lbnQ9eyIkY29udGFp
bnMiOnF1ZXJ5fSkKICAgICAgICAKICAgICAgICByZXR1cm4ganNvbmlmeShyZXN1bHQpCgogICAg
ZGVmIHJlbW92ZV9kYXRhKHNlbGYscXVlcnkpOgogICAgICAgIGNvbGxlY3Rpb24gPSBzZWxmLl9f
Y2xpZW50LmdldF9vcl9jcmVhdGVfY29sbGVjdGlvbihuYW1lPXNlbGYuX19jb2xsZWN0aW9uKQog
ICAgICAgIGNvbGxlY3Rpb24uZGVsZXRlKCB3aGVyZV9kb2N1bWVudD17IiRjb250YWlucyI6c3Ry
KHF1ZXJ5KX0pCgogICAgICAgIG9wZXJhdGlvbiA9IHsib3BlcmF0aW9uIjoiY29uY2x1ZGVkIn0K
ICAgICAgICByZXR1cm4ganNvbmlmeShvcGVyYXRpb24pCgogICAgZGVmIGRlbGV0ZV9jb2xsZWN0
aW9uKHNlbGYpOgogICAgICAgIHNlbGYuX19jbGllbnQuZGVsZXRlX2NvbGxlY3Rpb24obmFtZT1z
ZWxmLl9fY29sbGVjdGlvbikKCiAgICAgICAgb3BlcmF0aW9uID0geyJvcGVyYXRpb24iOiJjb25j
bHVkZWQifQogICAgICAgIHJldHVybiBqc29uaWZ5KG9wZXJhdGlvbikKCiAgICBkZWYgdXBkYXRl
X2RhdGEoc2VsZixpZHNfY29sbGVjdGlvbixtZXRhZGF0YSxkb2N1bWVudCk6CiAgICAgICAgY29s
bGVjdGlvbiA9IHNlbGYuX19jbGllbnQuZ2V0X29yX2NyZWF0ZV9jb2xsZWN0aW9uKG5hbWU9c2Vs
Zi5fX2NvbGxlY3Rpb24pCiAgICAgICAgY29sbGVjdGlvbi51cGRhdGUoaWRzPWlkc19jb2xsZWN0
aW9uLG1ldGFkYXRhcz1tZXRhZGF0YSxkb2N1bWVudHM9ZG9jdW1lbnQpCgogICAgICAgIG9wZXJh
dGlvbiA9IHsib3BlcmF0aW9uIjoiY29uY2x1ZGVkIn0KICAgICAgICByZXR1cm4ganNvbmlmeShv
cGVyYXRpb24pCiAgICAgICAgCgoKICAgIGRlZiB0cmFpbihzZWxmLHF1ZXJ5LG1vZGVsKToKICAg
ICAgICAKICAgICAgICBjb2xsZWN0aW9uID0gc2VsZi5fX2NsaWVudC5nZXRfb3JfY3JlYXRlX2Nv
bGxlY3Rpb24obmFtZT1zZWxmLl9fY29sbGVjdGlvbikKICAgICAgICByZXN1bHQgPSBjb2xsZWN0
aW9uLnF1ZXJ5KHF1ZXJ5X3RleHRzPXF1ZXJ5LHdoZXJlX2RvY3VtZW50PXsiJGNvbnRhaW5zIjpx
dWVyeX0saW5jbHVkZT1bImRvY3VtZW50cyJdKQogICAgICAgIAogICAgICAgIGZvciBpdGVtIGlu
IHJlc3VsdFsiZG9jdW1lbnRzIl06CiAgICAgICAgICAgIHByaW50KGl0ZW0pCiAgICAgICAgICAg
IGtub3dsZWRnZV9kYXRhID0geyJtb2RlbCI6bW9kZWwsImlucHV0IjppdGVtfSAgICAKICAgICAg
ICAgICAgZW1iZWRkaW5nX2RhdGEgPSByZXF1ZXN0cy5wb3N0KCJodHRwOi8vbG9jYWxob3N0OjEx
NDM0L2FwaS9lbWJlZGRpbmdzIixqc29uPWtub3dsZWRnZV9kYXRhKQoKICAgICAgICBvcGVyYXRp
b24gPSB7Im9wZXJhdGlvbiI6ImNvbmNsdWRlZCJ9CiAgICAgICAgcmV0dXJuIGpzb25pZnkob3Bl
cmF0aW9uKQoKCiAgICBkZWYgd2ViX2NvbGxlY3Rpb24oc2VsZixxdWVyeSk6CiAgICAgICAgCiAg
ICAgICAgY29sbGVjdGlvbiA9IHNlbGYuX19jbGllbnQuZ2V0X29yX2NyZWF0ZV9jb2xsZWN0aW9u
KG5hbWU9c2VsZi5fX2NvbGxlY3Rpb24pCiAgICAgICAgbWV0YWRhdGEgPSB7InNlYXJjaGZyb20i
OiJ3ZWIifQogICAgICAgIHRvcGljX2lkID0gc3RyKHF1ZXJ5KQoKICAgICAgICBkdWNrX2R1Y2tf
c2VhcmNoID0gZHVja2R1Y2tnb19zZWFyY2guRERHUygpLnRleHQocXVlcnksbWF4X3Jlc3VsdHM9
NSkKICAgICAgICBtYXRlcmlhbF90b19sZWFybiA9IFtdCgogICAgICAgIGZvciBzZWFyY2hfcmVz
dWx0IGluIGR1Y2tfZHVja19zZWFyY2g6CiAgICAgICAgICAgIG1hdGVyaWFsX3RvX2xlYXJuLmFw
cGVuZChzZWFyY2hfcmVzdWx0WyJib2R5Il0pCgogICAgICAgIGNvdW50ZXIgPSAwCgogICAgICAg
IGZvciBpdGVtIGluIG1hdGVyaWFsX3RvX2xlYXJuOgogICAgICAgICAgICBpZHNfbGlzdCA9IFtd
CiAgICAgICAgICAgIAogICAgICAgICAgICBpZHNfbGlzdC5hcHBlbmQodG9waWNfaWQrIl8iK3N0
cihjb3VudGVyKSkKICAgICAgICAgICAgY29sbGVjdGlvbi5hZGQoZG9jdW1lbnRzID0gaXRlbSxt
ZXRhZGF0YXM9IG1ldGFkYXRhLGlkcz0gaWRzX2xpc3QpCgogICAgICAgICAgICBpZHNfbGlzdC5j
bGVhcigpCiAgICAgICAgICAgIGNvdW50ZXIgPSBjb3VudGVyICsgMQoKICAgICAgICBvcGVyYXRp
b24gPSB7Im9wZXJhdGlvbiI6ImNvbmNsdWRlZCJ9CiAgICAgICAgcmV0dXJuIGpzb25pZnkob3Bl
cmF0aW9uKQ==
    """

def vectoragent():
    return  str("""
aW1wb3J0IGFnZW50CmltcG9ydCB2ZWN0b3JtYW5hZ2VyCgpjbGFzcyB2ZWN0b3JBZ2VudChhZ2Vu
dC5hZ2VudCk6CiAgICAKICAgIGRlZiBfX2luaXRfXyhzZWxmLG5hbWVfY29sbGVjdGlvbixkYXRh
X3B1dCx0b3BpYyx0b3BpY19pZCk6CiAgICAgICAgc2VsZi5fX25hbWVjb2xsZWN0aW9uID0gbmFt
ZV9jb2xsZWN0aW9uCiAgICAgICAgc2VsZi5fX2RhdGFwbGFpbiA9IGRhdGFfcHV0CiAgICAgICAg
c2VsZi5fX3RvcGljID0gdG9waWMKICAgICAgICBzZWxmLl9fdG9waWNpZCA9IHRvcGljX2lkCgog
ICAgZGVmIGRvVmVjdG9yKHNlbGYpOgogICAgICAgIHZlY3RvciA9IHZlY3Rvcm1hbmFnZXIudmVj
dG9yTWFuYWdlcihzZWxmLl9fbmFtZWNvbGxlY3Rpb24pCiAgICAgICAgcmV0dXJuIHZlY3Rvci5h
ZGRfb3JfY3JlYXRlX2RhdGEoZGF0YT1zZWxmLl9fZGF0YXBsYWluLHRvcGljPXNlbGYuX190b3Bp
Yyx0b3BpY19pZD1zZWxmLl9fdG9waWNpZCkgICAgICAgCiAgICAgICAgIAogICAgZGVmIGdldFZl
Y3RvcihzZWxmKToKICAgICAgICB2ZWN0b3IgPSB2ZWN0b3JtYW5hZ2VyLnZlY3Rvck1hbmFnZXIo
c2VsZi5fX25hbWVjb2xsZWN0aW9uKQogICAgICAgIHJldHVybiAgdmVjdG9yLmdpdmVfZGF0YShz
ZWxmLl9fdG9waWMsc2VsZi5fX2RhdGFwbGFpbikKCiAgICBkZWYgcmVtb3ZlVmVjdG9yKHNlbGYs
cXVlcnkpOgogICAgICAgIHZlY3RvciA9IHZlY3Rvcm1hbmFnZXIudmVjdG9yTWFuYWdlcihzZWxm
Ll9fbmFtZWNvbGxlY3Rpb24pCiAgICAgICAgcmV0dXJuIHZlY3Rvci5yZW1vdmVfZGF0YShxdWVy
eSkKCiAgICBkZWYgcmVtb3ZlQ29sbGVjdGlvbihzZWxmKToKICAgICAgICB2ZWN0b3IgPSB2ZWN0
b3JtYW5hZ2VyLnZlY3Rvck1hbmFnZXIoc2VsZi5fX25hbWVjb2xsZWN0aW9uKSAgICAgICAKICAg
ICAgICByZXR1cm4gdmVjdG9yLmRlbGV0ZV9jb2xsZWN0aW9uKCkKCiAgICBkZWYgcG9wdWxhdGVX
ZWJWZWN0b3Ioc2VsZixzZWFyY2hfcXVlcnkpOgogICAgICAgIHZlY3RvciA9IHZlY3Rvcm1hbmFn
ZXIudmVjdG9yTWFuYWdlcihzZWxmLl9fbmFtZWNvbGxlY3Rpb24pCiAgICAgICAgcmV0dXJuIHZl
Y3Rvci53ZWJfY29sbGVjdGlvbihzZWFyY2hfcXVlcnkpCiAgICAgICAgCiAgICBkZWYgdXBkYXRl
VmVjdG9yKHNlbGYpOgogICAgICAgIHZlY3RvciA9IHZlY3Rvcm1hbmFnZXIudmVjdG9yTWFuYWdl
cihzZWxmLl9fbmFtZWNvbGxlY3Rpb24pCiAgICAgICAgcmV0dXJuIHZlY3Rvci51cGRhdGVfZGF0
YShzZWxmLl9fdG9waWNpZCxzZWxmLl9fdG9waWMsc2VsZi5fX2RhdGFwbGFpbikKCiAgICBkZWYg
dHJhaW5MTE0oc2VsZixxdWVyeSxtb2RlbCk6CiAgICAgICAgdmVjdG9yID0gdmVjdG9ybWFuYWdl
ci52ZWN0b3JNYW5hZ2VyKHNlbGYuX19uYW1lY29sbGVjdGlvbikKICAgICAgICByZXR1cm4gdmVj
dG9yLnRyYWluKHF1ZXJ5LG1vZGVsKQ==
    """)
