
---
title: 'PikaScript v1.10.0 发布，轻量级跨平台嵌入式 Python 引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9194'
author: 开源中国
comments: false
date: Fri, 05 Aug 2022 15:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9194'
---

<div>   
<div class="content">
                                                                                            <p>PikaScript v1.10.0 已经发布，轻量级跨平台嵌入式 Python 引擎。</p> 
<p>此版本更新内容包括：</p> 
<h1>功能更新：</h1> 
<h2>性能</h2> 
<ul> 
 <li>速度提升高达78%</li> 
</ul> 
<h2>语言</h2> 
<ul> 
 <li> <p>初步支持"try...except" #169</p> </li> 
 <li> <p>支持 0bxxx字面值 #171</p> </li> 
 <li> <p>支持像 String('test').split('t') 这样的函数链</p> </li> 
 <li> <p>支持切片嵌套，如 a = x[y[z]] #173</p> </li> 
 <li> <p>支持切片链，如 a[x][y] #174</p> </li> 
 <li> <p>支持 function()[x] #177</p> </li> 
 <li> <p>支持元组字面值 #178</p> </li> 
 <li> <p>支持绑定来自其他 *.py (除main.py外)引入的 .pyi</p> </li> 
 <li> <p>支持 del 关键字 <a href="https://gitee.com/Lyon1998/pikascript/issues/I5KDES" target="_blank">https://gitee.com/Lyon1998/pikascript/issues/I5KDES</a></p> </li> 
</ul> 
<h2>库</h2> 
<ul> 
 <li>支持binascii #176</li> 
 <li>支持open() 内置函数 #181</li> 
 <li>支持 windows 和 linux 的sleep()#186</li> 
</ul> 
<h1>错误修复：</h1> 
<ul> 
 <li>错误：打印（无）返回其他字符串 #175</li> 
 <li>错误：对于循环错误继续后的内部循环 #179</li> 
 <li>错误：当 arg 大小 > int16_t 时堆栈错误 #185</li> 
 <li>一些python运算符操作不正确或不符合预期 <a href="https://gitee.com/Lyon1998/pikascript/issues/I5JN75" target="_blank">https://gitee.com/Lyon1998/pikascript/issues/I5JN75</a></li> 
 <li>[dict] 中的 输出不正确 <a href="https://gitee.com/Lyon1998/pikascript/issues/I5JWSR" target="_blank">https://gitee.com/Lyon1998/pikascript/issues/I5JWSR</a></li> 
</ul> 
<h1>不兼容的更新：</h1> 
<ul> 
 <li>.pyi 生成的函数的入口参数顺序可能发生更改</li> 
</ul> 
<h2>迁移指南：</h2> 
<ul> 
 <li>更新C模块中入口参数的顺序。</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/Lyon1998/pikascript/releases/v1.10.0">https://gitee.com/Lyon1998/pikascript/releases/v1.10.0</a></p>
                                        </div>
                                      
</div>
            