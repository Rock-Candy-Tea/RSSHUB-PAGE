
---
title: 'Phalcon v5.0 发布，PHP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9979'
author: 开源中国
comments: false
date: Mon, 26 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9979'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Phalcon 是一个开源的 Web 框架，作为 PHP 语言的 C 语言扩展，提供高性能和低资源消耗。Phalcon 团队在 2020 年 5 月底开始了 v5 版本的开发工作。时隔两年，v5.0 稳定版正式发布。</p> 
<h3>变化</h3> 
<ul> 
 <li>改变了 <code>Phalcon\\\\Logger\\\\Adapter\\\\Stream::process</code> 来打开日志文件、检查锁、写入内容并关闭流</li> 
 <li>把 getters 和 setters 从速记格式改为完整方法</li> 
 <li>将 <code>Phalcon\\\\Annotations\\\\Reflection</code> 类方法的返回类型改为 <code>array</code></li> 
 <li>改变了 <code>Phalcon\\\\Html\\\\Escaper::attributions()</code> 也接受一组属性</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>修复并改进了 <code>object</code> 和 <code>?object</code> 返回类型</li> 
 <li>修复了 <code>Phalcon\\\\Filter\\\\Validation\\\\Validator\\\\Digit</code> ，以在调用 <code>ctype_*</code> 时只使用字符串</li> 
 <li>修复了 <code>Phalcon\\\\Flash\\\\AbstractFlash::outputMessage</code> 返回消息</li> 
 <li>修复了 <code>Phalcon\\\\Filter\\\\Validation\\\\Validator\\\\Numericality</code>，以正确检测字符串数字中的非法字符</li> 
 <li>修复了 <code>Phalcon\\\\Mvc\\\\Model</code> 类的反射中的分段错误</li> 
 <li>修复了反射的分段错误</li> 
</ul> 
<h3>添加</h3> 
<ul> 
 <li>添加了 <code>Phalcon\\\\Encryption\\\\Security\\\\JWT\\\\Token::validate()</code>，以验证一个令牌的声明</li> 
 <li>添加了 <code>Phalcon\\\\Encryption\\\\Security\\\\JWTToken::verify()</code> 来验证令牌的签名</li> 
 <li>增加了 <code>Phalcon\\\\Encryption\\\\Security\\\\JWT\\\\Validator::getErrors()</code>，以数组形式返回验证的任何错误</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphalcon%2Fcphalcon%2Freleases%2Ftag%2Fv5.0.0" target="_blank">https://github.com/phalcon/cphalcon/releases/tag/v5.0.0</a></p>
                                        </div>
                                      
</div>
            