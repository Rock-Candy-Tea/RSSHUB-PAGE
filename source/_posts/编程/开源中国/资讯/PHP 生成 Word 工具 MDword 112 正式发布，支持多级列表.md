
---
title: 'PHP 生成 Word 工具 MDword 1.1.2 正式发布，支持多级列表'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/12422458/111026036-1c647700-8423-11eb-9df2-e9a2e5530007.png'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 11:46:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/12422458/111026036-1c647700-8423-11eb-9df2-e9a2e5530007.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start">MDword 是PHP生成word的另一工具。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">更新日志（用法详见<a href="https://gitee.com/colin_86/MDword/blob/main/tests/samples/simple%20for%20readme/index.php">案例</a>）</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持多级列表（支持段落式样赋值）</li> 
 <li>优化目录跳转</li> 
 <li>已知bug修复</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">主要用途：动态生成word<br> 优势：生成word只需关注动态数据及逻辑，无需关注式样的调整（式样可以借助office word调整母版即可）</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">与PHPWord的爱恨情仇</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">共同点</h3> </li> 
</ul> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>PHP编写的库（资源包）</li> 
 <li>用于生成office word</li> 
</ol> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">不同点</h3> </li> 
</ul> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>PHPWord 专注于一个元素一个元素的写入，而MDword则是专注于在母版的基础上修改，功能更强大，编码效率更高</li> 
 <li>修改文字式样，增加封面，修改页眉页脚MDword只需用word编辑软件调整母版，而PHPWord需要繁琐的去调整每个元素</li> 
 <li>可以自动生成目录</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">教程</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">安装</h3> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6a737d">//方法一</span></span>
<span>composer <span style="color:#d73a49">require</span> mkdreams/mdword</span>
<span><span style="color:#6a737d">//方法二，手动引入自动加载类</span></span>
<span><span style="color:#d73a49">require_once</span>(<span style="color:#032f62">'Autoloader.php'</span>);</span></pre> 
 </div> 
</div> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">给母版“temple.docx”添加批注</h3> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="image" src="https://user-images.githubusercontent.com/12422458/111026036-1c647700-8423-11eb-9df2-e9a2e5530007.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">调用方法（更多更丰富的调用方式，参考案例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmaster%2Ftests%2Fsamples%2Fsimple%2520for%2520readme%2Findex.php" target="_blank">tests\samples\simple for readme</a>，例如：目录、序号等）</h3> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6a737d">//新建类 加载 母版</span></span>
<span>$TemplateProcessor = <span style="color:#d73a49">new</span> WordProcessor();</span>
<span>$template = <span style="color:#032f62">'temple.docx'</span>;</span>
<span>$TemplateProcessor->load($template);</span>

<span><span style="color:#6a737d">//赋值</span></span>
<span>$TemplateProcessor->setValue(<span style="color:#032f62">'value'</span>, <span style="color:#032f62">'r-value'</span>);</span>

<span><span style="color:#6a737d">//克隆并复制</span></span>
<span>$TemplateProcessor->clones(<span style="color:#032f62">'people'</span>, <span>3</span>);</span>

<span>$TemplateProcessor->setValue(<span style="color:#032f62">'name#0'</span>, <span style="color:#032f62">'colin0'</span>);</span>
<span>$TemplateProcessor->setValue(<span style="color:#032f62">'name#1'</span>, [</span>
<span>    [<span style="color:#032f62">'text'</span>=><span style="color:#032f62">'colin1'</span>,<span style="color:#032f62">'style'</span>=><span style="color:#032f62">'style'</span>,<span style="color:#032f62">'type'</span>=>MDWORD_TEXT],</span>
<span>    [<span style="color:#032f62">'text'</span>=><span>1</span>,<span style="color:#032f62">'type'</span>=>MDWORD_BREAK],</span>
<span>    [<span style="color:#032f62">'text'</span>=><span style="color:#032f62">'86'</span>,<span style="color:#032f62">'style'</span>=><span style="color:#032f62">'style'</span>,<span style="color:#032f62">'type'</span>=>MDWORD_TEXT]</span>
<span>]);</span>
<span>$TemplateProcessor->setValue(<span style="color:#032f62">'name#2'</span>, <span style="color:#032f62">'colin2'</span>);</span>

<span>$TemplateProcessor->setValue(<span style="color:#032f62">'sex#1'</span>, <span style="color:#032f62">'woman'</span>);</span>

<span>$TemplateProcessor->setValue(<span style="color:#032f62">'age#0'</span>, <span style="color:#032f62">'280'</span>);</span>
<span>$TemplateProcessor->setValue(<span style="color:#032f62">'age#1'</span>, <span style="color:#032f62">'281'</span>);</span>
<span>$TemplateProcessor->setValue(<span style="color:#032f62">'age#2'</span>, <span style="color:#032f62">'282'</span>);</span>

<span><span style="color:#6a737d">//图片复制</span></span>
<span>$TemplateProcessor->setImageValue(<span style="color:#032f62">'image'</span>, dirname(<span style="color:#d73a49">__FILE__</span>).<span style="color:#032f62">'/logo.jpg'</span>);</span>

<span><span style="color:#6a737d">//删除某行</span></span>
<span>$TemplateProcessor->deleteP(<span style="color:#032f62">'style'</span>);</span>

<span><span style="color:#6a737d">//保存</span></span>
<span>$rtemplate = <span style="color:#d73a49">__DIR__</span>.<span style="color:#032f62">'/r-temple.docx'</span>;</span>
<span>$TemplateProcessor->saveAs($rtemplate);</span></pre> 
 </div> 
</div> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">结果</h3> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="image" src="https://user-images.githubusercontent.com/12422458/111026037-1d95a400-8423-11eb-81e2-941f6b854e34.png" referrerpolicy="no-referrer"></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0">动图</h3> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="image" src="https://user-images.githubusercontent.com/12422458/111026041-1ec6d100-8423-11eb-8e14-d8daf99a9704.gif" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">性能情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Fperformance%2Findex.php" target="_blank">统计脚本</a>）</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>测试项</th> 
   <th>用时(S)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1页母版赋值100次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.04</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1页母版赋值500次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.16</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1页母版赋值1000次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.33</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1页母版赋值10000次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">7.80</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1750页母版赋值100次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4.61</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1750页母版赋值500次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4.94</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1750页母版赋值1000次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">5.43</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1750页母版赋值10000次</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">17.39</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">内存使用情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Fmemory%2520use%2Findex.php" target="_blank">统计脚本</a>）</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>连续运行第几次</th> 
   <th>累积内存使用情况</th> 
   <th>备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050590515136719 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">首次需要加载PHP类</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">5</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">6</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">7</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">8</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更多案例</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fsimple%2520for%2520readme" target="_blank">简单的综合案例</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Ftext" target="_blank">带式样的文字</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fimage" target="_blank">添加图片</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fclone" target="_blank">克隆</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fblock" target="_blank">多种方式设置区块，解决无法添加批注问题</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Ftree%2Fmaster%2Ftests%2Fsamples%2Fphpword" target="_blank">PHPWORD写入到区块</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Ftoc" target="_blank">目录嵌入到表格</a></li> 
</ul>
                                        </div>
                                      
</div>
            