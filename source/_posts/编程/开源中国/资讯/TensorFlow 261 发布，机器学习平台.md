
---
title: 'TensorFlow 2.6.1 发布，机器学习平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7320'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7320'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">TensorFlow 是一个用于机器学习的端到端开源平台。它有一个全面灵活的工具、库和社区资源所组成的生态，让开发人员轻松建立和部署由 ML 驱动的应用程序。TensorFlow 最初用于进行机器学习和深度神经网络研究。但该系统具有足够的通用性，也适用于其他广泛的领域。</p> 
<h3 style="margin-left:0px"><strong>2.6.1 主要更新内容：</strong></h3> 
<ul> 
 <li>修复了<code>saved_model_cli</code> 中的代码注入问题。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41228" target="_blank">CVE-2021-41228</a> )</li> 
 <li>修复了使用未初始化的值而导致的漏洞。 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41225" target="_blank">CVE-2021-41225</a> )</li> 
 <li>修复<code>FusedBatchNorm</code> 内核中的堆 OOB。 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41223" target="_blank">CVE-2021-41223</a> )</li> 
 <li>修复了任意内存读入<code>ImmutableConst</code> 的问题。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41227" target="_blank">CVE-2021-41227</a> )</li> 
 <li>修复了<code>SparseBinCount</code> 中的堆 OOB 。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41226" target="_blank">CVE-2021-41226</a> )</li> 
 <li>修复了<code>SparseFillEmptyRows</code>中的堆 OOB 。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41224" target="_blank">CVE-2021-41224</a> ) </li> 
 <li>修复了由于<code>SplitV</code> 中的负拆分导致的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41222" target="_blank">段错误</a>。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41222" target="_blank">CVE-2021-41222</a> )</li> 
 <li>修复了在<code>Cudnn*</code>ops 的形状推断期间，访问无效内存导致的段错误和漏洞。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41221" target="_blank">CVE-2021-41221</a> )</li> 
 <li>修复了<code>Exit</code>节点前面没有<code>Enter</code>op 时的空指针异常。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41217" target="_blank">CVE-2021-41217</a> )</li> 
 <li>修复了<code>tf.raw_ops.AllToAll</code>中被 0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41218" target="_blank">整除</a>的问题。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41218" target="_blank">CVE-2021-41218</a> ) </li> 
 <li>修复了 <code>CollectiveReduceV2</code> 释放后的使用和内存泄漏问题。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41220" target="_blank">CVE-2021-41220</a> )</li> 
 <li>通过 <code>nullptr</code> 稀疏矩阵乘法中的引用绑定来修复未定义的行为( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41219" target="_blank">CVE-2021-41219</a> )</li> 
 <li>修复了<code>Transpose</code>中的堆缓冲区溢出。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41216" target="_blank">CVE-2021-41216</a> ) </li> 
 <li>防止相互递归 <code>tf.function</code> 对象引起的死锁。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41213" target="_blank">CVE-2021-41213</a> )</li> 
 <li>修复了<code>DeserializeSparse</code> 中的空指针异常。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41215" target="_blank">CVE-2021-41215</a> )</li> 
 <li>修复了从 <code>nullptr</code>  <span style="color:#2e3033">引用绑定</span>到 <code>tf.ragged.cross</code> 引发的未定义行为。 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41214" target="_blank">CVE-2021-41214</a> )</li> 
 <li>修复了读取 <code>tf.ragged.cross</code> 的堆 OOB 。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41212" target="_blank">CVE-2021-41212</a> )</li> 
 <li>修复了 <code>QuantizeV2</code> 形状推断中的堆 OOB。 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41211" target="_blank">CVE-2021-41211</a>）</li> 
 <li>修复了所有<code>tf.raw_ops.QuantizeAndDequantizeV*</code> 操作中的堆 OOB 读取( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41205" target="_blank">CVE-2021-41205</a> )</li> 
 <li>修复了<code>ParallelConcat</code> 中的 FPE。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41207" target="_blank">CVE-2021-41207</a> ) </li> 
 <li>使用零尺寸滤波器修复卷积的 FPE 问题。 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41209" target="_blank">CVE-2021-41209</a> )</li> 
 <li>修复了读入 <code>tf.raw_ops.SparseCountSparseOutput</code> 的堆 OOB。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41210" target="_blank">CVE-2021-41210</a> )</li> 
 <li><span style="color:#2e3033">修复了增强树代码中不完全验证导致的漏洞。</span> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41208" target="_blank">CVE-2021-41208</a> )</li> 
 <li>修复了多个 TF 操作中形状验证不完整导致的漏洞 。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41206" target="_blank">CVE-2021-41206</a> )</li> 
 <li><span style="color:#2e3033">修复复制常量资源张量时产生的段错误。</span>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41204" target="_blank">CVE-2021-41204</a> )</li> 
 <li>修复了 <code>EinsumHelper::ParseEquation</code> 中由单元化访问引起的漏洞。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41201" target="_blank">CVE-2021-41201</a> ) </li> 
 <li>修复了由于检查点加载期间缺少验证，而导致的多个漏洞和段错误。 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41203" target="_blank">CVE-2021-41203</a> )</li> 
 <li>修复了在<code>tf.range </code>中产生崩溃的溢出。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41202" target="_blank">CVE-2021-41202</a> ) </li> 
 <li>修复了在<code>tf.image.resize</code>大小较大时，导致崩溃的溢出。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41199" target="_blank">CVE-2021-41199</a> )</li> 
 <li>修复了 <code>tf.tile</code>当平铺张量很大时导致崩溃的溢出。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41198" target="_blank">CVE-2021-41198</a> )</li> 
 <li>修复了 <code>tf.summary.create_file_writer</code> 中验证不完整而产生的漏洞。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41200" target="_blank">CVE-2021-41200</a> )</li> 
 <li>修复了 <code>CHECK</code> 在具有大张量形状的操作中，由于溢出和失败而导致的多次崩溃。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41197" target="_blank">CVE-2021-41197</a> )</li> 
 <li>修复了 <code>max_pool3d</code> 当 size 参数为 0 或负数时的崩溃。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41196" target="_blank">CVE-2021-41196</a> )</li> 
 <li>修复了 <code>tf.math.segment_*</code> 操作崩溃。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41195" target="_blank">CVE-2021-41195</a> )</li> 
 <li>更新<code>curl</code> 到 <code>7.78.0</code> 版本，以处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-22922" target="_blank">CVE-2021-22922</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-22923" target="_blank">CVE-2021-22923</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-22924" target="_blank">CVE-2021-22924</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-22925" target="_blank">CVE-2021-22925</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-22926" target="_blank">CVE-2021-22926</a>。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow%2Freleases%2Ftag%2Fv2.6.1" target="_blank">https://github.com/tensorflow/tensorflow/releases/tag/v2.6.1</a></p>
                                        </div>
                                      
</div>
            