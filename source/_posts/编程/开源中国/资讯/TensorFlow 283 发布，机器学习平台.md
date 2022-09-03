
---
title: 'TensorFlow 2.8.3 发布，机器学习平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1964'
author: 开源中国
comments: false
date: Sat, 03 Sep 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1964'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">TensorFlow 是一个用于机器学习的端到端开源平台。它有一个全面灵活的工具、库和社区资源所组成的生态，让开发人员轻松建立和部署由 ML 驱动的应用程序。TensorFlow 最初用于进行机器学习和深度神经网络研究。但该系统具有足够的通用性，也适用于其他广泛的领域。</p> 
<h3 style="margin-left:0px"><strong>2.8.3 主要更新内容：</strong></h3> 
<ul> 
 <li>修复了由溢出导致的 tf.reshape 中的 CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35934" target="_blank">CVE-2022-35934</a><span style="color:#24292f">)</span></li> 
 <li>修复了由于缺少验证导致的 SobolSample 中的 CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35935" target="_blank">CVE-2022-35935</a><span style="color:#24292f">)</span></li> 
 <li>修复了 TF Lite 中 Gather_nd 操作中的 OOB 读取 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35937" target="_blank">CVE-2022-35937</a><span style="color:#24292f">)</span></li> 
 <li>修复了因缺少验证而导致的 TensorListReserve CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35960" target="_blank">CVE-2022-35960</a><span style="color:#24292f">)</span></li> 
 <li>修复了 TF Lite 中 Scatter_nd 操作中的 OOB 写入<span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35939" target="_blank">CVE-2022-35939</a><span style="color:#24292f">)</span></li> 
 <li>修复了 RaggedRangeOp 中的整数溢出 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35940" target="_blank">CVE-2022-35940</a><span style="color:#24292f">)</span></li> 
 <li>修复了 AvgPoolOp 中的 CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35941" target="_blank">CVE-2022-35941</a><span style="color:#24292f">)</span></li> 
 <li>修复 UnbatchGradOp 中的 CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35952" target="_blank">CVE-2022-35952</a><span style="color:#24292f">)</span></li> 
 <li>修复了每通道量化转置卷积上的段错误 TFLite 转换器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-36027" target="_blank">CVE-2022-36027</a><span style="color:#24292f">)</span></li> 
 <li>修复了 AvgPool3DGrad 中的 CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35959" target="_blank">CVE-2022-35959</a><span style="color:#24292f">)</span></li> 
 <li>修复了 FractionalAvgPoolGrad 中的 CHECK 失败 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35963" target="_blank">CVE-2022-35963</a><span style="color:#24292f">)</span></li> 
 <li>修复 BlockLSTMGradV2 中的段错误 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2022-35963" target="_blank">CVE-2022-35963</a><span style="color:#24292f">)</span></li> 
 <li>修复了 QuantizeAndDequantizeV3 中的 CHECK 失败 (CVE-2022-36026)</li> 
</ul> 
<p>更多修复项请阅读<span style="color:#333333">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow%2Freleases%2Ftag%2Fv2.8.3" target="_blank">https://github.com/tensorflow/tensorflow/releases/tag/v2.8.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            