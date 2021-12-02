
---
title: 'JsoupXpath v2.5.1 发布，HTML 解析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7625'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 11:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7625'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">简介</h2> 
<p style="color:#24292f; text-align:start"><strong>JsoupXpath</strong><span> </span>是一款纯Java开发的使用xpath解析提取html数据的解析器，针对html解析完全重新实现了W3C XPATH 1.0标准语法，xpath的Lexer和Parser基于Antlr4构建，html的DOM树生成采用Jsoup，故命名为JsoupXpath. 为了在java里也享受xpath的强大与方便但又苦于找不到一款足够好用的xpath解析器，故开发了JsoupXpath。JsoupXpath的实现逻辑清晰，扩展方便， 支持完备的W3C XPATH 1.0标准语法，W3C规范：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.w3.org%2FTR%2F1999%2FREC-xpath-19991116" target="_blank">http://www.w3.org/TR/1999/REC-xpath-19991116</a><span> </span>，JsoupXpath语法描述文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhegexiaohuozi%2FJsoupXpath%2Fblob%2Fmaster%2Fsrc%2Fmain%2Fresources%2FXpath.g4" target="_blank">Xpath.g4</a></p> 
<h2>更新内容</h2> 
<ul> 
 <li>修复了 PrecedingSiblingOneSelector 这个函数无效的问题 ， 感谢<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fs24963386" target="_blank">@s24963386</a>贡献！</li> 
 <li>修复<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhegexiaohuozi%2FJsoupXpath%2Fissues%2F66" target="_blank">#Issue66</a><span> </span>，函数参数表达式使用的上下文不够全面的问题</li> 
 <li>优化<code>text()</code><span> </span>块节点属性信息，以便更好的支持倒序索引</li> 
 <li>增加<code>double/long sum(node-set)</code><span> </span>函数，计算给定的节点集合中数字节点值的和，计算参数范围内包含非数字内容则计算无效。</li> 
 <li>优化<code>num()</code>结果表现，尽量符合用户使用直觉。整数返回整数，浮点数返回浮点数，不再统一只返回浮点数。</li> 
</ul> 
<p>相关Test：</p> 
<pre><code class="language-java">    @Test
    public void issue64And65()&#123;
        String content = "<div class='a'>1</div>\n" +
                "<div>2</div>\n" +
                "<div class='a'>3</div>\n" +
                "<div>4</div>\n" +
                "<div>5</div>";
        JXDocument j = JXDocument.create(content);
        Assert.assertEquals("2", j.selNOne("//div[text()='3']/preceding-sibling-one::div/text()").asString());
        Assert.assertEquals("4", j.selNOne("//div[text()='3']/following-sibling-one::div/text()").asString());
    &#125;

    @Test
    public void issue66() throws Exception &#123;
        JXDocument j = JXDocument.create(FileUtils.readFileToString(new File(loader.getResource("issue66.html").toURI()), Charset.forName("utf8")));
        logger.info("&#123;&#125;", j.selN("count(//bookstore/book)"));
        logger.info("&#123;&#125;", j.selN("//bookstore/book[position()<count(//bookstore/book)]/price"));
        logger.info("&#123;&#125;", j.selN("//bookstore/book[position()<count(//bookstore/book)-1]/price"));
        logger.info("&#123;&#125;", j.selN("sum(//bookstore/book/year[num()<2005])"));
        logger.info("&#123;&#125;", j.selN("sum(//bookstore/book/price)"));
        logger.info("&#123;&#125;", j.selN("sum(//bookstore/book/title)"));
        Assert.assertEquals(4,j.selNOne("count(//bookstore/book)").asLong().longValue());
        Assert.assertEquals(3,j.selN("//bookstore/book[position()<count(//bookstore/book)]/price").size());
        Assert.assertEquals(2,j.selN("//bookstore/book[position()<count(//bookstore/book)-1]/price").size());
        Assert.assertEquals(4006,j.selNOne("sum(//bookstore/book/year[num()<2005])").asLong().longValue());
        Assert.assertEquals("",j.selNOne("sum(//bookstore/book/title)").asString());
    &#125;</code></pre> 
<h2>写在最后</h2> 
<p>欢迎大家贡献新特性</p>
                                        </div>
                                      
</div>
            