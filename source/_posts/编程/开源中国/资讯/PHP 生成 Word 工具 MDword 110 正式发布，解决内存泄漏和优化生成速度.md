
---
title: 'PHP 生成 Word 工具 MDword 1.1.0 正式发布，解决内存泄漏和优化生成速度'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/12422458/111026036-1c647700-8423-11eb-9df2-e9a2e5530007.png'
author: 开源中国
comments: false
date: Wed, 25 Aug 2021 09:17:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/12422458/111026036-1c647700-8423-11eb-9df2-e9a2e5530007.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">MDword 是PHP生成word的另一工具。</p> 
<h2 style="text-align:start">更新日志</h2> 
<ul> 
 <li>优化大母版生成速度</li> 
 <li>解决内存泄漏问题</li> 
</ul> 
<p style="text-align:left"><em><strong>性能情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Fperformance%2Findex.php" target="_blank">统计脚本</a>）</strong></em></p> 
<table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th>测试项</th> 
   <th>用时(S)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值100次</td> 
   <td style="border-color:#dfe2e5">0.04</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值500次</td> 
   <td style="border-color:#dfe2e5">0.16</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值1000次</td> 
   <td style="border-color:#dfe2e5">0.33</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值10000次</td> 
   <td style="border-color:#dfe2e5">7.80</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值100次</td> 
   <td style="border-color:#dfe2e5">4.61</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值500次</td> 
   <td style="border-color:#dfe2e5">4.94</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值1000次</td> 
   <td style="border-color:#dfe2e5">5.43</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值10000次</td> 
   <td style="border-color:#dfe2e5">17.39</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left"><em><strong>内存使用情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Fmemory%2520use%2Findex.php" target="_blank">统计脚本</a>）</strong></em></p> 
<table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th>连续运行第几次</th> 
   <th>累积内存使用情况</th> 
   <th>备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">1</td> 
   <td style="border-color:#dfe2e5">0.050590515136719 M</td> 
   <td style="border-color:#dfe2e5">首次需要加载PHP类</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">3</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">4</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">5</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">6</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">7</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">8</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">项目介绍</h2> 
<p style="text-align:left">主要用途：动态生成word<br> 优势：生成word只需关注动态数据及逻辑，无需关注式样的调整（式样可以借助office word调整母版即可）</p> 
<h2 style="text-align:left">与PHPWord的爱恨情仇</h2> 
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
 <li>PHPWord 专注于一个元素一个元素的写入，而MDword则是专注于在母版的基础上修改，功能更强大，编码效率更高</li> 
 <li>修改文字式样，增加封面，修改页眉页脚MDword只需用word编辑软件调整母版，而PHPWord需要繁琐的去调整每个元素</li> 
 <li>可以自动生成目录</li> 
</ol> 
<h2 style="text-align:left">教程</h2> 
<ul> 
 <li> <h3>安装</h3> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre>//方法一
composer require mkdreams/mdword
//方法二，手动引入自动加载类
require_once('Autoloader.php');</pre> 
 </div> 
</div> 
<ul> 
 <li> <h3>给母版“temple.docx”添加批注</h3> </li> 
</ul> 
<p style="text-align:left"><img alt="image" src="https://user-images.githubusercontent.com/12422458/111026036-1c647700-8423-11eb-9df2-e9a2e5530007.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3>调用方法（更多更丰富的调用方式，参考案例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmaster%2Ftests%2Fsamples%2Fsimple%2520for%2520readme%2Findex.php" target="_blank">tests\samples\simple for readme</a>，例如：目录、序号等）</h3> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre>//新建类 加载 母版
$TemplateProcessor = new WordProcessor();
$template = 'temple.docx';
$TemplateProcessor->load($template);

//赋值
$TemplateProcessor->setValue('value', 'r-value');

//克隆并复制
$TemplateProcessor->clones('people', 3);

$TemplateProcessor->setValue('name#0', 'colin0');
$TemplateProcessor->setValue('name#1', [
    ['text'=>'colin1','style'=>'style','type'=>MDWORD_TEXT],
    ['text'=>1,'type'=>MDWORD_BREAK],
    ['text'=>'86','style'=>'style','type'=>MDWORD_TEXT]
]);
$TemplateProcessor->setValue('name#2', 'colin2');

$TemplateProcessor->setValue('sex#1', 'woman');

$TemplateProcessor->setValue('age#0', '280');
$TemplateProcessor->setValue('age#1', '281');
$TemplateProcessor->setValue('age#2', '282');

//图片复制
$TemplateProcessor->setImageValue('image', dirname(__FILE__).'/logo.jpg');

//删除某行
$TemplateProcessor->deleteP('style');

//保存
$rtemplate = __DIR__.'/r-temple.docx';
$TemplateProcessor->saveAs($rtemplate);</pre> 
 </div> 
</div> 
<ul> 
 <li> <h3>结果</h3> </li> 
</ul> 
<p style="text-align:left"><img alt="image" src="https://user-images.githubusercontent.com/12422458/111026037-1d95a400-8423-11eb-81e2-941f6b854e34.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3>动图</h3> </li> 
</ul> 
<p style="text-align:left"><img alt="image" src="https://user-images.githubusercontent.com/12422458/111026041-1ec6d100-8423-11eb-8e14-d8daf99a9704.gif" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">性能情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Fperformance%2Findex.php" target="_blank">统计脚本</a>）</h2> 
<table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th>测试项</th> 
   <th>用时(S)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值100次</td> 
   <td style="border-color:#dfe2e5">0.04</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值500次</td> 
   <td style="border-color:#dfe2e5">0.16</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值1000次</td> 
   <td style="border-color:#dfe2e5">0.33</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1页母版赋值10000次</td> 
   <td style="border-color:#dfe2e5">7.80</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值100次</td> 
   <td style="border-color:#dfe2e5">4.61</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值500次</td> 
   <td style="border-color:#dfe2e5">4.94</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值1000次</td> 
   <td style="border-color:#dfe2e5">5.43</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1750页母版赋值10000次</td> 
   <td style="border-color:#dfe2e5">17.39</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">内存使用情况（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmkdreams%2FMDword%2Fblob%2Fmain%2Ftests%2Fsamples%2Fmemory%2520use%2Findex.php" target="_blank">统计脚本</a>）</h2> 
<table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th>连续运行第几次</th> 
   <th>累积内存使用情况</th> 
   <th>备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">1</td> 
   <td style="border-color:#dfe2e5">0.050590515136719 M</td> 
   <td style="border-color:#dfe2e5">首次需要加载PHP类</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">3</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">4</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">5</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">6</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">7</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">8</td> 
   <td style="border-color:#dfe2e5">0.050949096679688 M</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">更多案例</h2> 
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
            