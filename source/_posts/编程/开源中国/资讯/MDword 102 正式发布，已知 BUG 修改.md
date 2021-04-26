
---
title: 'MDword 1.0.2 正式发布，已知 BUG 修改'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202103/19101313_3vPQ.png'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 09:37:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202103/19101313_3vPQ.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">MDword 是PHP生成word的另一工具。</p> 
<h2 style="text-align:start">更新日志</h2> 
<p>BUG修复：</p> 
<ul> 
 <li>特殊字符导致word无法正常打开。</li> 
 <li>克隆段落存在bug。</li> 
 <li>支持保留未使用的批注。</li> 
 <li>只存在“$&#123;name/&#125;”标记，没有批注的情况下，替换内容无效。</li> 
</ul> 
<h2 style="text-align:start">项目介绍</h2> 
<p style="text-align:start"><span style="color:#000000">主要用途：动态生成word<br> 优势：生成word只需关注动态数据及逻辑，无需关注式样的调整（式样可以借助office word调整母版即可）</span></p> 
<h2 style="text-align:start">与PHPWord的爱恨情仇</h2> 
<ul> 
 <li> <h3>共同点</h3> </li> 
</ul> 
<ol> 
 <li>PHP编写的库（资源包）</li> 
 <li>用于生成office word</li> 
</ol> 
<ul> 
 <li> <h3>不同点</h3> </li> 
</ul> 
<ol> 
 <li>PHPWord 需要一个元素一个元素的写入，而MDword则是在母版的基础上修改，编码效率更高</li> 
 <li>修改文字式样，增加封面，修改页眉页脚MDword只需用word编辑软件调整母版，而PHPWord需要繁琐的去调整每个元素</li> 
</ol> 
<h2 style="text-align:start">教程</h2> 
<ul> 
 <li> <h3>安装</h3> </li> 
</ul> 
<pre style="text-align:start"><code><span style="color:#6a737d"><span style="color:#6a737d">//方法一</span></span>
composer <span style="color:#d73a49"><span style="color:#d73a49">require</span></span> mkdreams/mdword
<span style="color:#6a737d"><span style="color:#6a737d">//方法二，手动引入自动加载类</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">require_once</span></span>(<span style="color:#032f62"><span style="color:#032f62">'Autoloader.php'</span></span>);
</code></pre> 
<ul> 
 <li> <h3>给母版“temple.docx”添加批注</h3> </li> 
</ul> 
<p style="text-align:start"><img alt="image" src="https://static.oschina.net/uploads/img/202103/19101313_3vPQ.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3>调用方法（可参考此实例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmaster%2Ftests%2Fsamples%2Fsimple%2520for%2520readme%2Findex.php" target="_blank">tests\samples\simple for readme</a>）</h3> </li> 
</ul> 
<pre style="text-align:start"><code><span style="color:#6a737d"><span style="color:#6a737d">//新建类 加载 母版</span></span>
$TemplateProcessor = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> WordProcessor();
$template = <span style="color:#032f62"><span style="color:#032f62">'temple.docx'</span></span>;
$TemplateProcessor->load($template);

<span style="color:#6a737d"><span style="color:#6a737d">//赋值</span></span>
$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'value'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'r-value'</span></span>);

<span style="color:#6a737d"><span style="color:#6a737d">//克隆并复制</span></span>
$TemplateProcessor->clones(<span style="color:#032f62"><span style="color:#032f62">'people'</span></span>, 3);

$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'name#0'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'colin0'</span></span>);
$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'name#1'</span></span>, [[<span style="color:#032f62"><span style="color:#032f62">'text'</span></span>=><span style="color:#032f62"><span style="color:#032f62">'colin1'</span></span>,<span style="color:#032f62"><span style="color:#032f62">'style'</span></span>=><span style="color:#032f62"><span style="color:#032f62">'style'</span></span>,<span style="color:#032f62"><span style="color:#032f62">'type'</span></span>=>MDWORD_TEXT]]);
$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'name#2'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'colin2'</span></span>);

$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'sex#1'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'woman'</span></span>);

$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'age#0'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'280'</span></span>);
$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'age#1'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'281'</span></span>);
$TemplateProcessor->setValue(<span style="color:#032f62"><span style="color:#032f62">'age#2'</span></span>, <span style="color:#032f62"><span style="color:#032f62">'282'</span></span>);

<span style="color:#6a737d"><span style="color:#6a737d">//图片复制</span></span>
$TemplateProcessor->setImageValue(<span style="color:#032f62"><span style="color:#032f62">'image'</span></span>, dirname(<span style="color:#d73a49"><span style="color:#d73a49">__FILE__</span></span>).<span style="color:#032f62"><span style="color:#032f62">'/logo.jpg'</span></span>);

<span style="color:#6a737d"><span style="color:#6a737d">//删除某行</span></span>
$TemplateProcessor->deleteP(<span style="color:#032f62"><span style="color:#032f62">'style'</span></span>);

<span style="color:#6a737d"><span style="color:#6a737d">//保存</span></span>
$rtemplate = <span style="color:#d73a49"><span style="color:#d73a49">__DIR__</span></span>.<span style="color:#032f62"><span style="color:#032f62">'/r-temple.docx'</span></span>;
$TemplateProcessor->saveAs($rtemplate);</code></pre> 
<ul> 
 <li> <h3>结果</h3> </li> 
</ul> 
<p style="text-align:start"><img alt="image" src="https://static.oschina.net/uploads/img/202103/19101313_R6V1.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3>动图</h3> </li> 
</ul> 
<p style="text-align:start"><img alt="image" src="https://static.oschina.net/uploads/img/202103/19101314_PE4w.gif" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">更多案例</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fsimple%2520for%2520readme" target="_blank">简单的综合案例</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Ftext" target="_blank">带式样的文字</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fimage" target="_blank">添加图片</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fclone" target="_blank">克隆</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fblock" target="_blank">多种方式设置区块，解决无法添加批注问题</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fphpword" target="_blank">PHPWORD写入到区块</a></li> 
</ul>
                                        </div>
                                      
</div>
            