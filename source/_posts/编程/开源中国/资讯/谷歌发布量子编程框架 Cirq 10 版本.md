
---
title: '谷歌发布量子编程框架 Cirq 1.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1155'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1155'
---

<div>   
<div class="content">
                                                                                            <p>7 月 19 日，谷歌宣布开源量子编程框架 Cirq 的第一个完整版本 ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquantumai.google%2Fcirq" target="_blank">Cirq 1.0 正式发布</a>。</p> 
<p>Cirq 是一个 Python 框架，用于编写、操作和优化量子电路。它专为近期的量子计算机设计，这些计算机具有几百个量子比特和几千个量子门，而 Cirq 1.0 版本支持这些系统的绝大多数工作流，并且有一个稳定的 API，谷歌称后续只会在主要版本号的更改时更新该 API。</p> 
<p>Cirq 使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsemver.org%2F" target="_blank">语义版本控制</a>，这意味着 Cirq 的未来点版本将与完整版本兼容。例如，Cirq 1.1 版不会对 1.0 版的 Cirq 界面进行重大更改；只有在主要版本更改（例如从 1.x 到 2.0）才会发生重大变化。</p> 
<p>Cirq 代码示例：</p> 
<pre><code class="language-python">import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)</code></pre> 
<p>现在已经基于 Cirq 建立了一个健康的社区，支持不同的量子计算研究领域。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fquantumlib%2FCirq%2Fnetwork%2Fdependents%3Fpackage_id%3DUGFja2FnZS03MzM0NTIzNA%253D%253D" target="_blank">这些库</a>包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tensorflow.org%2Fquantum" target="_blank">TensorFlow Quantum</a>：探索量子机器学习的工具。使用 TensorFlow Quantum，研究人员以每秒 1.1 petaflops（每秒 1.1 x 1015 次操作）的速度在 30 个量子位上训练了一个机器学习模型。</li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquantumai.google%2Fopenfermion" target="_blank">OpenFermion</a>：用于化学模拟中涉及量子计算的开源工具。</li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcqcl.github.io%2Ftket%2Fpytket%2Fapi%2Findex.html" target="_blank">Pytket</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Fpytket-cirq" target="_blank">pytkey-cirq</a> )：用于优化和操作量子电路的开源 Python 工具。</li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmitiq.readthedocs.io%2Fen%2Fv.0.1a2%2Fread_README.html" target="_blank">Mitiq</a>：由非营利 Unitary 基金开发的开源库，用于由非营利 Unitary 基金开发的错误缓解技术。</li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquantumai.google%2Fqsim" target="_blank">Qsim</a>：使用 AVX/FMA 矢量化指令编写的高性能状态矢量模拟器，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquantumai.google%2Fqsim%2Ftutorials%2Fgcp_gpu" target="_blank">可选 GPU 加速</a>。</li> 
</ul> 
<p> </p> 
<p>有关 Cirq  1.0 的更多内容，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopensource.googleblog.com%2F2022%2F07%2FCirq-Turns-1.0.html" target="_blank">谷歌博客</a>和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fquantumlib%2FCirq%2Freleases%2Ftag%2Fv1.0.0" target="_blank">1.0 发行说明</a> 。</p>
                                        </div>
                                      
</div>
            