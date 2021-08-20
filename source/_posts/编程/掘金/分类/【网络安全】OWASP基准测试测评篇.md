
---
title: '【网络安全】OWASP基准测试测评篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6b3590673c46b9b2bfe5dd89d0d23c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 03:24:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6b3590673c46b9b2bfe5dd89d0d23c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><strong>一、背景</strong></h1>
<p>源代码静态分析工具(SAST)作为软件安全的重要保障工具，已经在各个领域被广泛使用。随着开源SAST工具的广泛使用，工具种类的增加，使用者很难判断工具的优劣及适不适合企业的应用场景，本文从金融、互联网企业最常用的Java语言代码分析的角度，对静态分析进行一次简要的测评，为大家选择静态分析工具提供依据，此外，本文分析了目前静态代码分析工具存在的技术问题及工具评估的基本准则。</p>
<h1 data-id="heading-1"><strong>二、概述</strong></h1>
<p>一般来说，误报和漏报率是SAST最重要的技术评价指标，但由于没有通用意义上的测试集能够全面反应静态分析工具在检测精度能力方面高低暨分析的敏感度。由此，为了简化测试难度，本次测评我们选择了一个Java语言且偏安全的国际通用测试集OWASP benchmark，以反应代码分析工具在Java安全检测能力上的强弱。</p>
<p>OWASP基准测试是一个示例应用程序，其中包含来自11个类别的数千个漏洞。基准测试中包括很难通过静态分析处理的代码片段，例如：间接调用、不可达分支、映射、依赖于配置文件的值。</p>
<p>用例下载地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fgithub.com%252FOWASP%252FBenchmark%252Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOWASP%2FBenchmark%2Freleases" ref="nofollow noopener noreferrer">github.com/OWASP/Bench…</a>，可以在一定程度上反应代码分析工具的检测能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6b3590673c46b9b2bfe5dd89d0d23c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1. 测试依据</strong></p>
<p>下表为某款工具的OWASP检测结果，如图所示，左侧一列表示所有类别，P/N为正/负样本数(badcase/goodcase)，TP/FP为真/假阳性的数量(badcase报出数/误报数)，TN/FN是真/假阴性的数量（good case报出数/漏报数），TPR和FPR是正确率和误报率，Y是约登指数，约登指数( Youden’s indx，YI)即正确指数，此指数值的范围只从0~1，约登指数越大， 其真实性亦越好。其中TPR、FPR、Y的计算公式如下：</p>
<p>TPR=TP/P</p>
<p>FPR=FP/N</p>
<p>   Y=[TP/(TP+FN)+TN/(FP+TN)]-1</p>

































































































































































<table><thead><tr><th>类别</th><th>P</th><th>N</th><th>TP</th><th>FP</th><th>TN</th><th>FN</th><th>TPR</th><th>FPR</th><th>Y</th></tr></thead><tbody><tr><td>Command Injection (cmdi)</td><td>126</td><td>125</td><td>126</td><td>45</td><td>80</td><td>0</td><td>1.0</td><td>0.36</td><td>0.64</td></tr><tr><td>Weak Cryptography (crypto)</td><td>130</td><td>116</td><td>130</td><td>0</td><td>116</td><td>0</td><td>1.0</td><td>0.0</td><td>1.0</td></tr><tr><td>Weak Randomness (hash)</td><td>129</td><td>107</td><td>129</td><td>0</td><td>107</td><td>0</td><td>1.0</td><td>0.0</td><td>1.0</td></tr><tr><td>LDAP Injection (ldapi)</td><td>27</td><td>32</td><td>27</td><td>13</td><td>19</td><td>0</td><td>1.0</td><td>0.41</td><td>0.59</td></tr><tr><td>Path Traversal (pathtraver)</td><td>133</td><td>135</td><td>133</td><td>36</td><td>99</td><td>0</td><td>1.0</td><td>0.27</td><td>0.73</td></tr><tr><td>Secure Cookie Flag   securecookie)</td><td>36</td><td>31</td><td>36</td><td>0</td><td>31</td><td>0</td><td>1.0</td><td>0.0</td><td>1.0</td></tr><tr><td>SQL Injection (sqli)</td><td>272</td><td>232</td><td>272</td><td>87</td><td>145</td><td>0</td><td>1.0</td><td>0.375</td><td>0.63</td></tr><tr><td>Trust Boundary Violation   (trustbound)</td><td>83</td><td>43</td><td>83</td><td>24</td><td>19</td><td>0</td><td>1.0</td><td>0.56</td><td>0.44</td></tr><tr><td>Weak Randomization (weakrand)</td><td>218</td><td>275</td><td>218</td><td>0</td><td>275</td><td>0</td><td>1.0</td><td>0.0</td><td>1.0</td></tr><tr><td>XPATH Injection (xpathi)</td><td>15</td><td>20</td><td>15</td><td>7</td><td>13</td><td>0</td><td>1.0</td><td>0.35</td><td>0.65</td></tr><tr><td>Cross Site Scripting (xss)</td><td>246</td><td>209</td><td>246</td><td>48</td><td>161</td><td>0</td><td>1.0</td><td>0.23</td><td>0.77</td></tr><tr><td>Average All</td><td>1415</td><td>1325</td><td>1415</td><td>290</td><td>1035</td><td>0</td><td>1.0</td><td>0.23</td><td>0.77</td></tr></tbody></table>
<p><strong>2. 测试结果</strong></p>
<p>选取市场上主流的SAST工具进行测试，本次选取的测试工具涵盖较广，包含国外商业工具、开源工具以及国内自研工具。如SonarQube[1]代码自动审查工具，该工具是开源工具中使用最多的工具，因为开源免费尤其受很多金融企业喜爱；以色列的Checkmarx CxSAST[2]，Micro Focus Fortify[3]，目前在电力、金融等行业推广较多，是中国市场Java应用最多的工具之一；还有在互联网领域应用的比较广泛的新思科技的Coverity[4]、IBM Appscan[5]。军工领域应用比较广泛的Parasoft的JTest[6]、VeraCode[7]等。下图是10款静态分析工具的OWASP基准测试结果。商业SAST工具01-06包括：Checkmarx CxSAST、Micro Focus Fortify、IBM AppScan Source、Coverity Code Advisor、Parasoft Jtest、SourceMeter[9]和Veracode工具。</p>
<p> </p>


















































































<table><thead><tr><th>分析工具</th><th>OWASP版本</th><th>TPR</th><th>FPR</th><th>Y</th></tr></thead><tbody><tr><td>FBwfindSecBugs[10]</td><td>1.2</td><td>0.97</td><td>0.58</td><td>0.39</td></tr><tr><td>SonarQube</td><td>1.2</td><td>0.5</td><td>0.17</td><td>0.33</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttp%253A%252F%252Fwww.redrocket.cn%252FHome%252FProduct_introduction%252Findex.html%253Fid%253D2" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.redrocket.cn%2FHome%2FProduct_introduction%2Findex.html%3Fid%3D2" ref="nofollow noopener noreferrer">鸿渐SAST</a></td><td>1.2</td><td>1.0</td><td>0.12</td><td>0.88</td></tr><tr><td>SAST-04</td><td>1.1</td><td>0.61</td><td>0.29</td><td>0.33</td></tr><tr><td>SAST-06</td><td>1.1</td><td>0.85</td><td>0.52</td><td>0.33</td></tr><tr><td>SAST-02</td><td>1.1</td><td>0.56</td><td>0.26</td><td>0.31</td></tr><tr><td>SAST-03</td><td>1.1</td><td>0.46</td><td>0.214</td><td>0.25</td></tr><tr><td>SAST-05</td><td>1.1</td><td>0.48</td><td>0.29</td><td>0.19</td></tr><tr><td>SAST-01</td><td>1.1</td><td>0.29</td><td>0.12</td><td>0.17</td></tr><tr><td>PMD</td><td>1.2</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></tbody></table>
<p>从上图可知，覆盖率指数最大为1（即100%覆盖，不存在漏报）；而误报率最低的指数为0.12，最高为0.58,尚无。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e5125ac65c44d90a1894e36fa38ef09~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2"><strong>三、技术分析</strong></h1>
<p>静态代码分析基本原理：首先将源代码解析为抽象语法树；采用控制流分析、多态分析、指向分析、函数调用分析等多种分析算法对基本分析模型；考虑路径敏感等多种情况，建立符号执行、抽象解释、图可达性等程序模型；根据缺陷模式在程序模型的基础上生成一阶逻辑表达式并采用SMT进行可满足性约束求解，生成最终结果。目前很多工具只做基本分析层面，尤其是开源工具，针对全模式的敏感分析很多工具并不支持，或支持的不好，因此可能产生大量的误漏报，下面分析了几种典型的问题：</p>
<p>基于以上要点，分析误报原因，了解工具的局限性。通过分析，误报基本由以下几种情况导致。</p>
<p><strong>1. 集合覆盖问题</strong></p>
<p>在集合中，部分集合数据存在污染数据，当检索集合中未污染部分时，导致整个集合覆盖污染，误报产生。如：以下代码中，map中填充带有一个污点（param）和一个未污点的值（a_value），并且从映射中检索参数赋值给bar。如果一个集合的一部分被污染了，假设整个collection都被污染，那么在本例中，当我们检索集合的未污染部分时，导致误报。</p>
<pre><code class="copyable">private class Test &#123;
  public String doSomething(String param) throws ServletException, IOException &#123;
        String bar = "safe!";
        java.util.HashMap map831 = new java.util.HashMap();
        map831.put("keyA-831", "a_Value"); // put some stuff in the collection
        map831.put("keyB-831", param); // put it in a collection
        map831.put("keyC", "another_Value"); // put some stuff in the collection
        bar = (String)map831.get("keyB-831"); // get it back out
        bar = (String)map831.get("keyA-831"); // get safe value back out
        return bar;
     &#125;
  &#125; // end innerclass Test
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 集合过度污染问题</strong></p>
<p>在一个集合中，部分集合数据存在污染数据，当对集成做一些操作后，工具无法识别出受污染的数据，导致其他正常数据收到影响，产生误报。如：在以下代码中，存在一个未受污染的值（safe），一个受污染的值(param) 和另一个未受污染的值(moresafe) 被添加到列表中。 当第一个值“safe”被删除后，从列表的开头，检索索引为 1 的列表元素，即读取未受污染的值“moresafe”。同样导致误报。</p>
<pre><code class="copyable"> public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException &#123;
   response.setContentType("text/html");
   String param = "";
   boolean flag = true;
   java.util.Enumeration names = request.getParameterNames();
   while (names.hasMoreElements() && flag) &#123;
   String name = (String) names.nextElement();   
   String[] values = request.getParameterValues(name);
   if (values != null) &#123;
   for(int i=0;i<values.length && flag; i++)&#123;
   String value = values[i];
   if (value.equals("vector")) &#123;
   param = name;
      flag = false;
   &#125;
   &#125;
   &#125;
   &#125; 
   String bar = "alsosafe";
   if (param != null) &#123;
   java.util.List valuesList = new java.util.ArrayList( );
   valuesList.add("safe");
   valuesList.add( param );
   valuesList.add( "moresafe" ); 
   valuesList.remove(0); // remove the 1st safe value 
   bar = valuesList.get(1); // get the last 'safe' value
   &#125; 
   String cmd = org.owasp.benchmark.helpers.Utils.getInsecureOSCommandString(this.getClass().getClassLoader());
   String[] args = &#123;cmd&#125;;
          String[] argsEnv = &#123; bar &#125;;       
   Runtime r = Runtime.getRuntime();
   try &#123;
   Process p = r.exec(args, argsEnv, new java.io.File(System.getProperty("user.dir")));
   org.owasp.benchmark.helpers.Utils.printOSCommandResults(p, response);
   &#125; catch (IOException e) &#123;
   System.out.println("Problem executing cmdi - TestCase");
              throw new ServletException(e);
   &#125;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. 分支问题</strong></p>
<p>在条件分支中，由于条件设置问题，导致某些分支可能永远无法执行，若工具无法判定某些无法执行的分支，可能导致误报的产生。如：在以下代码中，因为num为常量106，（7*18）+num的值永远大于200，导致bar的值始终都为常量字符串，“This_should_always_happen”。另外一个包含污染数据的分支“param”永远无法执行。导致工具产生误报。</p>
<pre><code class="copyable"> private class Test &#123;
  public String doSomething(String param) throws ServletException, IOException &#123;
     String bar;// Simple ? condition that assigns constant to bar on true condition
     int num = 106;
     bar = (7*18) + num > 200 ? "This_should_always_happen" : param;
     return bar;
   &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1090656645784854ac078bc9b91936e0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></h1>
<h1 data-id="heading-4"><strong>四、结论</strong></h1>
<p>全面、高效地静态识别漏洞，减少工具的误报是静态分析中至关重要的技术，目前在该领域中，仍然有很大的进步空间。针对本次OWASP的基准测试，在选取的工具中，目前结果最好的工具覆盖率可以达到100%，且同时误报率为12%，也说明了工具正不断趋于成熟，但该结果仅针对OWASP测试用例。在后续的静态代码分析技术中，需要不断对静态数据流跟踪器进行持续优化，以此提高检测精度。</p>
<p>为了更好地对代码分析工具进行评价，笔者提出了几个评价维度，并给出评价等级：</p>











































































<table><thead><tr><th>评价指标</th><th>描述</th><th>Level 1</th><th>Level 2</th><th>Level 3</th></tr></thead><tbody><tr><td>约登指数</td><td>查全率-误报</td><td>0.9-1.0</td><td>0.7-0.9</td><td>0.7-</td></tr><tr><td>吞吐量</td><td>最大检测代码规模</td><td>1000W+</td><td>100W+</td><td>10W+</td></tr><tr><td>检测效率</td><td>每小时代码检测代码行数</td><td>100W+</td><td>50W+</td><td>10W+</td></tr><tr><td>片段代码检测能力</td><td>能否在编译不通过情况下检测</td><td>支持所有语言</td><td>C/C++,Java</td><td>不支持</td></tr><tr><td>并发检测能力</td><td>支持单CPU的多并发测试</td><td>硬件允许的最大值</td><td>单进程</td><td>单进程</td></tr><tr><td>跨语言及框架分析能力</td><td>支持最新的框架及兼容语言间调用</td><td>支持70种以上框架</td><td>支持10种以下</td><td>不支持</td></tr><tr><td>支持语言</td><td>支持检测的语言种类</td><td>20种+</td><td>10种+</td><td>3种+</td></tr><tr><td>与Devops集成能力</td><td>是否与DevOps主要工具集成</td><td>支持持续集成工具、版本管理及测试工具，三个方面</td><td>仅支持版本管理</td><td>不支持</td></tr><tr><td>CWE模式覆盖数</td><td>覆盖的缺陷模式个数</td><td>200+</td><td>100+</td><td>50+</td></tr></tbody></table>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4d2bda0166d453bb1efe61f254c864d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>最后</strong></p>
<p><strong>【<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fdocs.qq.com%252Fdoc%252FDVFNpaGJvRFJiQ2Ro" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDVFNpaGJvRFJiQ2Ro" ref="nofollow noopener noreferrer">相关资料详细</a>】</strong></p></div>  
</div>
            