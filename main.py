from gui import Apps

gui = Apps.Gui()

# from logics import regulafalsi, biseksi, secant
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# import numpy as np

# def exe(f):
#     f.set_function('3*x + np.sin(x) - math.e ** x')
#     f.compute(0,1.5,0.01)
#     # print('errors : ',f.get_errors())
#     # print('xr : ',f.get_xrs())
#     print('number of steps : ', len(f.get_xrs()), end='\t')
#     print('number of time taken (in nanoseconds) : ',f.get_exe_time())

# fb = biseksi.Biseksi()
# exe(fb)
# fr = regulafalsi.RegulaFalsi()
# exe(fr)
# fs = secant.Secant()
# exe(fs)

# # making plots
# fig = make_subplots(
#     rows=2, cols=3,
#     specs=[[{'colspan':2}, None, {"rowspan": 2}],
#            [{'colspan':2},None, None]],
#     subplot_titles=("Xrs Plot", "Execution Time Bar", "Errors Plot"))


# # Xrs plot
# fig.append_trace(go.Scatter(x=np.arange(1, fb.get_total_iter()), y=fb.get_xrs(),
#                     mode='lines+markers',
#                     name='Xr Biseksi'), row=1, col=1)
# fig.append_trace(go.Scatter(x=np.arange(1, fr.get_total_iter()), y=fr.get_xrs(),
#                     mode='lines+markers',
#                     name='Xr Regulafalsi'), row=1, col=1)
# fig.append_trace(go.Scatter(x=np.arange(1, fs.get_total_iter()), y=fs.get_xrs(),
#                     mode='lines+markers',
#                     name='Xr Secant'), row=1, col=1)

# # Errors plot
# fig.append_trace(go.Scatter(x=np.arange(1, fb.get_total_iter()), y=fb.get_errors(),
#                     mode='lines+markers',
#                     name='Err Biseksi'), row=2, col=1)
# fig.append_trace(go.Scatter(x=np.arange(1, fr.get_total_iter()), y=fr.get_errors(),
#                     mode='lines+markers',
#                     name='Err Regulafalsi'), row=2, col=1)
# fig.append_trace(go.Scatter(x=np.arange(1, fs.get_total_iter()), y=fs.get_errors(),
#                     mode='lines+markers',
#                     name='Err Secant'), row=2, col=1)

# # Running time bar
# fig.add_trace(go.Bar(name="Biseksi", y=['Biseksi'], x=[fb.get_exe_time()], orientation='h'),
#               row=1, col=3)
# fig.add_trace(go.Bar(name="Regulafalsi", y=['Regulafalsi'], x=[fr.get_exe_time()], orientation='h'),
#               row=1, col=3)
# fig.add_trace(go.Bar(name="Secant", y=['Secant'], x=[fs.get_exe_time()], orientation='h'),
#               row=1, col=3)

# fig.update_layout(
#     title='f(x) = '+str(fb.get_function()),
#     legend_title="Legend"
# )

# fig.show()
