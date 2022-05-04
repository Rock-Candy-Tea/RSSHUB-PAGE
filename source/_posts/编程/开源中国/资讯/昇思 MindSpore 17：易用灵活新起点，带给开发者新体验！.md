
---
title: '昇思 MindSpore 1.7：易用灵活新起点，带给开发者新体验！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0b490236ba5fb9ca04f4d8eb20f5b8f8557.png'
author: 开源中国
comments: false
date: Tue, 03 May 2022 23:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0b490236ba5fb9ca04f4d8eb20f5b8f8557.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#3e3e3e; margin-left:0; margin-right:0; text-align:justify"><span>经过社区开发者们的辛勤耕耘，我们马不停蹄地给大家递上昇思MindSpore最新的1.7版本。</span></p> 
<p style="color:#3e3e3e; margin-left:0; margin-right:0; text-align:justify"><span>在此版本中我们</span><span style="color:#0052ff"><strong>持续</strong></span><span style="color:#0052ff"><strong>提升框架易用性，简化安装过程，提供更丰富的文档和指导视频，帮助开发者快速上手；同时还提供了易用灵活的numpy模块，进一步提升昇思AI+科学计算的能力；此外，新版本还发布了计算机视觉工具库MindSpore Vision，并已支持一些主流网络</strong>，</span><span>让开发者极速体验基于昇思的应用。</span></p> 
<p style="color:#3e3e3e; margin-left:0; margin-right:0; text-align:justify"><span>下面就带大家详细了解下1.7版本的关键特性。</span></p> 
<h3 style="margin-left:0px; margin-right:0px"><strong>01 持续提升易用性，快速上手昇思MindSpore</strong></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>根据前期开发者访谈，我们在安装、文档、调试等方面对昇思MindSpore易用性进行了大量改进和提升，希望帮助开发者更快上手，更容易理解功能的原理、逻辑和特点，进而更方便高效地完成安装、开发、调试等任务。</span></p> 
<p style="margin-left:0; margin-right:0"><strong>1.1 简化安装</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span>昇思MindSpore1.7版本支持Mac（X86/M1）CPU，支持 Python 3.8（Windows/Linux/Mac），简化GPU版本依赖安装过程，并提供了一键式自动化脚本以及可操作性更强的安装指南。</span></p> 
<p style="margin-left:0; margin-right:0"><strong>1.2 优化丰富文档与手把手视频指导</strong></p> 
<p style="margin-left:0; margin-right:0"><strong><span>1)</span></strong><span>  1.7版本提供了超过<strong>1500个</strong>昇思MindSpore API文档的中文版，优化API文档可读性，提供更多的使用样例，能够帮助国内广大的开发者更好地理解功能原理和逻辑，也希望大家能够提出更多宝贵意见！</span></p> 
<pre><code>中文API文档地址：https://www.mindspore.cn/docs/zh-CN/master/api_python/mindspore.html</code></pre> 
<p style="margin-left:0; margin-right:0"><span><strong>2)</strong>  按照不同阶段的用户，对教程中数据处理、创建网络、模型训练等内容按照难易程度进行了重构。后续，我们会针对CV、NLP等领域，输出常用的端到端案例，也会输出教程对应的视频，方便大家学习和掌握。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>教程地址：https:<em>//www.mindspore.cn/tutorials/zh-CN/master/index.html</em></span></code></pre> 
<p style="margin-left:0; margin-right:0"><strong><span>3)</span></strong><span>  针对手把手安装与体验的系列视频，进行了系统优化和补充，内容涵盖安装、数据处理、模型训练/推理、调试等基础使用全流程。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>视频链接：https:<em>//www.mindspore.cn/resources/courses/list?id=47#title52</em></span></code></pre> 
<p style="margin-left:0; margin-right:0"><strong><span>4)</span></strong><span>  持续吸引开发者贡献技术干货帖，累计<strong>600+</strong>篇，同时系列博文包含机器学习、深度学习等基础知识，安装和数据处理等使用经验，累计<strong>39</strong>篇，供开发者搜索查看参考学习。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>干货地址：https:<em>//bbs.huaweicloud.com/forum/forum.php?mod=forumdisplay&orderby=lastpost&f</em></span></code></pre> 
<p style="margin-left:0; margin-right:0"><strong>1.3 支持“断点续训”，提供异常点CheckPoint保存能力</strong></p> 
<p style="margin-left:0; margin-right:0"><span>昇思MindSpore1.7版本提供了训练发生异常自动触发保存CheckPoint的能力，为开发者提供基于训练异常断点的恢复能力，实现“断点续训”与周期性保存CheckPoint功能可以同时使用，为开发者提供更多选择。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>详情参考：https:<em>//gitee.com/mindspore/docs/blob/r1.7/tutorials/source_zh_cn/advanced/train/save.i</em></span></code></pre> 
<p style="margin-left:0; margin-right:0"><strong>1.4 支持动态图Hook，提升网络调试效率 </strong></p> 
<p style="margin-left:0; margin-right:0"><span>为了方便用户在不改变网络结构的情况下，准确地感知深度学习网络各层数据的变化，从而快速地调试，昇思MindSpore在PyNative模式下设计了Hook功能。</span><span>用户使用Hook功能可以更方便地捕获中间层算子的输入、输出数据以及反向梯度变化。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:left"><span>在1.7版本中，PyNative模式针对Cell对象提供了register_forward_pre_hook、register_forward_hook和register_backward_hook功能。</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>1) </span></strong><span><span> </span>在Cell对象上使用 register_forward_pre_hook 接口来注册一个自定义的Hook函数，用来捕获正向传入该Cell对象的数据。</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>2)</span></strong><span>  在Cell对象上使用 register_forward_hook 接口来注册一个自定义的Hook函数，用来捕获正向传入Cell对象的数据和Cell对象的输出数据。</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>3)</span></strong><span>  在Cell对象上使用 register_backward_hook 函数来注册一个自定义的Hook函数，用来捕获网络反向传播时与Cell对象相关联的梯度。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>详情参考：https:<em>//gitee.com/mindspore/docs/blob/r1.7/tutorials/source_zh_cn/advanced/pynative_graph/pynative.ipynb</em></span></code></pre> 
<p style="margin-left:0; margin-right:0"><strong>1.5 优化模型开发体验</strong></p> 
<p style="margin-left:0; margin-right:0"><span>当前昇思MindSpore的nn层、ops算子等接口逐渐优化至臻，不管在静态图还是动态图中，都能使用更符合AI研究和开发人员的极简开发体验。</span><span>为此我们依托昇思MindSpore易用性SIG，未来将持续推出AI经典SOTA模型的昇思MindSpore最佳实践案例和视频，敬请期待。</span></p> 
<h3 style="margin-left:0px; margin-right:0px"><strong>02 提供易用灵活的numpy模块， 加速昇思MindSpore +科学计算</strong></h3> 
<p style="margin-left:0; margin-right:0"><span>mindspore.numpy模块包含一套完整的符合Numpy规范的接口，开发者可以使用Numpy的原生语法表达<span>昇思</span>MindSpore的模型，同时拥有<span>昇思</span>MindSpore的加速能力。</span></p> 
<p style="margin-left:0; margin-right:0"><span>为了更充分地展示mindspore.numpy在计算上的优势，我们提供了分子模拟库<span>昇思</span>MindSpore SPONGE的numpy重构版本。支持常见的系综模拟包含NVT、NPT等，例如进行新冠病毒Delta毒株模拟。所有的GPU核函数均完成了mindspore.numpy改写，以更好地展示分子动力学算法的运作机制，并方便研究人员扩展算法。</span></p> 
<p style="margin-left:0; margin-right:0"><span>重构后，代码量缩短50%以上。由于mindspore.numpy同时兼容了<span>昇思</span>MindSpore的其他加速特性，例如图编译加速以及图算融合，最终性能可以达到与原版本<span>昇思</span>MindSpore SPONGE相近的程度。</span></p> 
<p style="margin-left:0; margin-right:0"><span>mindspore.numpy, 不止是numpy的加速平替，更是构建神经网络的极简编程工具。numpy的大多数常用接口实际上也是神经网络构建中必不可少的构成，如Tensor创建接口ones, full, zeros等; 常用的Tensor操作concatenate，repeat，split等。</span></p> 
<p style="margin-left:0; margin-right:0"><span>在构造模型时，开发者不再需要每次实例化算子后调用，而可以选择使用mindspore.numpy中的接口，优雅地完成想要的功能。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>详情参考：https:<em>//www.mindspore.cn/docs/zh-CN/master/api_python/mindspore.numpy.html</em></span></code></pre> 
<h3 style="margin-left:0px; margin-right:0px"><strong>03 支持数据处理自适应调优，充分发挥数据处理性能</strong></h3> 
<p style="margin-left:0; margin-right:0"><span><span>昇思</span>MindSpore1.7版本提供了一种数据处理自动调优的工具——Dataset AutoTune。在训练过程中，此工具可以帮助用户根据系统环境资源的情况自动调整MindSpore Data数据处理管道的并行度和内存使用度，利用当前系统资源加快数据处理管道的处理速度。</span></p> 
<p style="margin-left:0; margin-right:0"><span>在整个网络训练的过程中，Dataset AutoTune工具会持续检测当前训练性能的瓶颈处于数据处理侧还是模型运算侧。如果检测到瓶颈在数据处理侧，则将进一步对数据处理管道中的各个操作（如GeneratorDataset、map、batch等）的参数进行调整，以加快该操作的计算速度。</span></p> 
<p style="margin-left:0; margin-right:0"><span>目前可调整的参数包括操作的并行度、内部队列深度/内存使用度，帮助用户加快模型训练的流程。未来，该工具会支持更多、更灵活的数据管道参数调整，包括异构算子加速、融合算子等，敬请期待。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0b490236ba5fb9ca04f4d8eb20f5b8f8557.png" referrerpolicy="no-referrer"></p> 
<pre><code>详情参考：https://gitee.com/mindspore/docs/blob/r1.7/tutorials/experts/source_zh_cn/debug/dataset_autotune.md</code></pre> 
<h3 style="margin-left:0px; margin-right:0px"><strong>04 MindSpore Vision——易用易理解的主流工具库</strong></h3> 
<p style="margin-left:0; margin-right:0"><span>MindSpore Vision是基于<span>昇思</span>MindSpore的开源计算机视觉研究工具库，MindSpore Vision已构筑基础的AI复用能力，支持部分主流、前沿网络，例如Efficientnet、Lenet、Mobilenetv2、Resnet、Vit等，提供手机侧推理与部署，欢迎开发者们参与贡献，共同拓展和维护MindSpore Vision，力争将其打造为易用易理解的主流工具库。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>详情参考：https:<em>//www.mindspore.cn/vision/docs/zh-CN/master/index.html</em></span></code></pre> 
<h3 style="margin-left:0px; margin-right:0px"><strong>05 支持蛋白质结构预测训练推理全流程，助力生物医药发展</strong></h3> 
<p style="margin-left:0; margin-right:0"><span><span>昇思</span>MindSpore与昌平实验室、北京大学生物医学前沿创新中心（BIOPIC）和化学与分子工程学院、深圳湾实验室高毅勤教授课题组（张骏、刘思睿等）及鹏城实验室陈杰团队基于全场景AI框架<span>昇思</span>MindSpore实现AlphaFold2蛋白质结构训练。</span></p> 
<p style="margin-left:0; margin-right:0"><span>联合工作依托鹏城云脑II昇腾AI集群进行，<strong>TM-score达87分（国际权威评测数据集CASP14），截止22年4月21日，在CAMEO竞赛中已连续三周取得第一</strong>，相关训练代码已在<span>昇思</span>MindSpore社区开源。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7dbef5e1b85e1969b80b063f0b0dcf66c32.png" referrerpolicy="no-referrer"></p> 
<p><span>T1052-D1 预测结构图（左）CASP14 87 targets TM-score 对比（右）</span></p> 
<p style="margin-left:0; margin-right:0"><span>采用昇腾基础软硬件平台后，在混合精度下，单步迭代时间由20秒缩短到12秒，性能提升超过60%。依托<span>昇思</span>MindSpore内存复用能力, 训练序列长度由384提升至512。</span></p> 
<p style="margin-left:0; margin-right:0"><span>为了尽可能客观地评估训练结果，<span>昇思</span>MindSpore选取了AlphaFold2论文附录中提到的87条验证集进行验证，平均TM-score达到87分，基本持平AlphaFold2。</span></p> 
<p style="margin-left:0; margin-right:0"><span><span>昇思</span>MindSpore将在算法、规模和软硬件支持等方向上持续改进，并计划开放共享训练数据集供同仁使用，也期望与更多学术界和工业界伙伴合作，进一步提升模型精度、扩展应用场景。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>代码仓链接：https:<em>//gitee.com/mindspore/mindscience/tree/dev/MindSPONGE/mindsponge/fold</em></span></code></pre> 
<h3 style="margin-left:0px; margin-right:0px"><strong>06 MindSpore Quantum：支持含噪声量子模拟器和量子线路的SVG绘制模式</strong></h3> 
<p style="margin-left:0; margin-right:0"><span>在当前NISQ阶段，真实量子比特的噪声还比较大，为了更准确的模拟真实的量子系统演化，在最新版本中，我们引入了噪声模拟功能，只用在量子线路中引入不同的噪声信道就能完成含噪量子模拟，从而使自己的模型更接近与真实情形，这些噪声信道包含泡利信道、比特翻转信道、相位反转信道等。</span></p> 
<p style="margin-left:0; margin-right:0"><span>此外我们还支持在Jupiter notebook中展示量子线路的svg格式图片，通过绘制精心设计的图片格式，可以直观地了解线路的构成并方便传播自己的量子算法。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e5977cc6b8eef7d7b3a1b44bb27e9ba603f.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span>左图是</span><span>构建一个贝尔态的量子线路，由于误差的存在，我们加入两个比特翻转信道来模拟量子系统的误差，并对这两个比特的量子态进行测量；</span></p> 
<p style="margin-left:0; margin-right:0"><span>右上图为该量子线路的SVG格式图片，右下图为量子线路采样结果图片。</span></p> 
<pre style="margin-left:0; margin-right:0"><code><span>API参考：https:<em>//www.mindspore.cn/mindquantum/docs/zh-CN/master/mindquantum.core</em></span></code></pre>
                                        </div>
                                      
</div>
            