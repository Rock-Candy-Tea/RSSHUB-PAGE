
---
title: 'ExcelUtil 3.1.8 发布，新增无注解读取功能，以及修复部分 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9571'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 13:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9571'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>你还在写大量的 Excel 导入导出代码？</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>ExcelUtil 一行代码搞定导入导出哦！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更多示例见官网哦，2.x 不建议观看，直接看 3.x 版本哦</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">【官网文档】<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.likaixuan.top%2FexcelUtil%2Fdoc%2Fv3" target="_blank">http://www.likaixuan.top/excelUtil/doc/v3</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>【本次更新内容如下】</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1. 新增无注解读取。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">原先需要在实体类打上@Excel(title="属性名称"）的注解，现在默认读取实体类的属性作为注解，</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#f39c12">TIPS：</span>如果实体类中出现一个属性有注解，则只取注解</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.允许Excel表头中的内容和实体类中属性不用一一对应</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">比如Excel中有5列 A | B | C | D | E </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">实体类是 B| D| E</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">也是支持的</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3.修复部分已知Bug</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多用法请参见官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.likaixuan.top%2FexcelUtil%2Fdoc%2Fv3" target="_blank">http://www.likaixuan.top/excelUtil/doc/v3</a><br> 以下用例都是 3.x 用法：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>一行代码搞定 Excel 导出且有水印！！！<br> <br> 就是这么简单！！！</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#bbb529"><span><span style="color:#032f62">/**</span>
 <span style="color:#032f62">*</span>
 <span style="color:#032f62">*</span> <span style="color:#032f62">参数说明：1.response</span> <span style="color:#032f62">没什么好说的</span>   <span>2.</span><span style="color:#032f62">list</span> <span style="color:#032f62">数据集</span>  <span>3</span><span style="color:#032f62">.导出excel的名称</span> <span>4</span><span style="color:#032f62">.自定义水印文字</span>
 <span style="color:#032f62">*/</span></span></span><span>
</span></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#bbb529">@GetMapping</span>(<span style="color:#d0d0ff">value </span>= <span style="color:#6a8759"><span style="color:#032f62">"/export"</span></span>)
<span style="color:#cc7832"><span><span style="color:#d73a49">public</span> <span style="color:#d73a49">void</span> </span></span><span style="color:#ffc66d"><span><span style="color:#6f42c1">testExport</span></span></span><span><span>(HttpServletResponse response)</span> </span><span style="color:#cc7832"><span>throws </span></span><span>Exception</span>&#123;
    
   List<PhoneModel> <span>list</span> = <span style="color:#cc7832"><span style="color:#d73a49">new</span> </span>ArrayList<>()<span style="color:#cc7832">;
</span><span style="color:#cc7832">   <span style="color:#d73a49">for</span></span>(<span style="color:#cc7832"><span style="color:#d73a49">int</span> </span>i=<span style="color:#6897bb"><span>0</span></span><span style="color:#cc7832">;</span>i<<span style="color:#6897bb"><span>10</span></span><span style="color:#cc7832">;</span>i++)&#123;
      PhoneModel model = <span style="color:#cc7832"><span style="color:#d73a49">new</span> </span>PhoneModel()<span style="color:#cc7832">;
</span><span style="color:#cc7832">      </span>model.setNum((i+<span style="color:#6897bb"><span>1</span></span>))<span style="color:#cc7832">;
</span><span style="color:#cc7832">      </span>model.setColor(<span style="color:#6a8759"><span style="color:#032f62">"</span></span><span style="color:#6a8759"><span style="color:#032f62">金色</span></span><span style="color:#6a8759"><span style="color:#032f62">"</span></span>+i)<span style="color:#cc7832">;
</span><span style="color:#cc7832">      </span>model.setPhoneName(<span style="color:#6a8759"><span style="color:#032f62">"</span></span><span style="color:#6a8759"><span style="color:#032f62">苹果</span></span><span style="color:#6a8759"><span style="color:#032f62">"</span></span>+i+<span style="color:#6a8759"><span style="color:#032f62">"S"</span></span>)<span style="color:#cc7832">;
</span><span style="color:#cc7832">      </span>model.setPrice(i)<span style="color:#cc7832">;
</span><span style="color:#cc7832">      </span>model.setSj(<span style="color:#cc7832"><span style="color:#d73a49">new</span> </span>Date())<span style="color:#cc7832">;
</span><span style="color:#cc7832">      </span><span>list</span>.add(model)<span style="color:#cc7832">;
</span><span style="color:#cc7832">   </span>&#125;
   <span style="color:#f1c40f"><strong>ExcelUtil.<em>exportExcelOutputStream</em>(response,<span>list</span>,PhoneModel.class,<span style="color:#032f62">"测试Excel导出"</span>,<span style="color:#032f62">"素剑步青尘"</span>);</strong></span><span style="color:#cc7832">
</span>&#125;
</pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>引入 pom</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#6a737d"><!-- https://mvnrepository.com/artifact/net.oschina.likaixuan/excelutil --></span>
<span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>net.oschina.likaixuan<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>excelutil<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.1.8<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></pre> 
<p> </p>
                                        </div>
                                      
</div>
            