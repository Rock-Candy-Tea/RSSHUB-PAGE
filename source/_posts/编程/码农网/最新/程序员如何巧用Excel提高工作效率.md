
---
title: '程序员如何巧用Excel提高工作效率'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/001.png'
author: 码农网
comments: false
date: Sun, 28 Apr 2019 13:28:42 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/001.png'
---

<div>   
<p>作为一名<span class="wp_keywordlink"><a href="http://www.codeceo.com/" title="程序员" target="_blank">程序员</a></span>，我们可能很少使用Excel，但是公司的一些职能部门，比如HR，财务等，使用Excel真的是太熟练了，以至于一些系统开发出来，导入和导出功能是使用最频繁的。</p>
<p>其实在程序开发的过程中，有些场景，我们也可以借助于Excel来大大的提升工作效率，比如以下场景：</p>
<ul>
<li>业务给一批数据，需要你批量更新下数据库</li>
<li>排查问题时，我们需要找出数据中的重复项</li>
<li>我们需要将一些内容按某个分隔符拆分成多列内容，以匹配不同的列</li>
</ul>
<p>接下来，我们详细讲解下具体的操作细节。</p>
<h2 id="拼接sql字符串">1.拼接Sql字符串</h2>
<p>在做开发的过程中，经常需要根据Excel中的数据去数据库查询，少量数据还可以去复制粘贴，大量数据时就需要将Excel中的数据拼接成自己需要的Sql，以提升工作效率。</p>
<h3 id="将某一列拼接成sql中的in条件">1.1：将某一列拼接成Sql中的In条件</h3>
<p>假设现在有如下的Excel数据，我需要从数据库中查询出这些门店的数据。</p>
<p><img class="aligncenter size-full wp-image-57015" title="001" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/001.png" alt width="322" height="474" referrerpolicy="no-referrer"></p>
<p>操作方法如下图所示：</p>
<p><img class="aligncenter size-full wp-image-57016" title="002" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/002.gif" alt width="800" height="700" referrerpolicy="no-referrer"></p>
<p>将生成的一列数据复制到Visual Studito Code中，进行替换即可</p>
<p><img class="aligncenter size-full wp-image-57017" title="003" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/003.gif" alt width="1030" height="698" referrerpolicy="no-referrer"></p>
<h3 id="将某一列拼接成c中的list">1.2：将某一列拼接成C#中的List</h3>
<p>假设现在有如下的Excel数据，我需要将这些值写在C#中的List中</p>
<p><img class="aligncenter size-full wp-image-57018" title="004" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/004.png" alt width="322" height="474" referrerpolicy="no-referrer"></p>
<p>操作方法如下图所示：</p>
<p><img class="aligncenter size-full wp-image-57019" title="005" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/005.gif" alt width="894" height="698" referrerpolicy="no-referrer"></p>
<p>将生成的一列数据复制到Visual Studito Code中，进行替换即可</p>
<p><img class="aligncenter size-full wp-image-57020" title="006" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/006.gif" alt width="894" height="698" referrerpolicy="no-referrer"></p>
<h3 id="拼接sql语句">1.3：拼接Sql语句</h3>
<p>你想想，哪天你正在工作呢，业务扔过来一个Excel，你一脸懵逼，以下是你们的对话：</p>
<blockquote><p>业务：帮我把系统里的某个字段改成Excel里的可以吗？我当时维护错了</p>
<p>你：你可以在系统里修改啊</p>
<p>业务：这么多数据，你让我一个一个改啊？而且很急，而且你还要考虑系统好用性，嘚吧嘚一大堆理由</p>
<p>你：内心深处，你是拒绝的，这明明是业务工作中的失误，现在却要你这个程序员来善后，事实上，你说：好的</p></blockquote>
<p>既然答应了，就得想着咋处理，数据如果只有几条，你复制粘贴还可以，如果是成千上万条呢，复制粘贴肯定不现实，累死你不说，还容易出错。</p>
<p>这时我们就可以借助于Excel来快速的拼接Sql。</p>
<p>假如有如下的Sql语句，现需要将Where条件中的StoreCode的值替换为Excel中的值。</p>
<pre class="brush: sql; gutter: true; first-line: 1">SELECT  st.StoreCode ,
        st.StoreName ,
        s.SellerName ,
        so.SellerOrgName
FROM    dbo.Fct_Store AS st
        INNER JOIN dbo.Fct_Seller AS s ON s.Disabled = 0
                                          AND st.SellerCode = s.SellerCode
        INNER JOIN dbo.Config_SellerOrg AS so ON so.Disabled = 0
                                                 AND s.SellerOrgCode = so.SellerOrgCode
WHERE   st.Disabled = 0
        AND st.StoreCode = '10000196';</pre>
<p>按照1.1和1.2中的方式，将Sql语句复制到Excel中，提示如下信息(<strong>如果语句长度少的话，不会出现</strong>)：</p>
<p><img class="aligncenter size-full wp-image-57021" title="007" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/007.gif" alt width="894" height="698" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-57022" title="008" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/008.png" alt width="824" height="159" referrerpolicy="no-referrer"></p>
<p>此时，就需要用到Excel中的<strong>CONCATENATE()</strong>函数,如下所示：</p>
<p><img class="aligncenter size-full wp-image-57023" title="009" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/009.gif" alt width="967" height="698" referrerpolicy="no-referrer"></p>
<h2 id="查找重复项">2.查找重复项</h2>
<p>在平时的开发工作中，我们有时会需要从Excel中查找出重复的数据，以便清理业务数据。</p>
<p>假如现在有如下图所示的文档，现需要找出<strong>“店铺编码”</strong>列的重复数据。</p>
<p><img class="aligncenter size-full wp-image-57024" title="010" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/010.png" alt width="327" height="573" referrerpolicy="no-referrer"></p>
<h3 id="新建规则">2.1新建规则</h3>
<p>选中列“店铺编码”,然后依次点击菜单：<strong>开始–>条件格式–>突出显示单元格规则–>重复值</strong></p>
<p><img class="aligncenter size-full wp-image-57025" title="011" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/011.png" alt width="1047" height="453" referrerpolicy="no-referrer"></p>
<h3 id="设置重复值格式">2.2设置重复值格式</h3>
<p>在“重复值”弹出框中，按照默认的样式点击确定，会发现重复项被标记出来</p>
<p><img class="aligncenter size-full wp-image-57026" title="012" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/012.png" alt width="350" height="154" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-57027" title="013" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/013.png" alt width="337" height="542" referrerpolicy="no-referrer"></p>
<h3 id="筛选重复数据">2.3筛选重复数据</h3>
<p>点击菜单：<strong>数据–>筛选</strong>，然后按照单元格颜色筛选，就可以只查看重复的数据</p>
<p><img class="aligncenter size-full wp-image-57028" title="014" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/014.png" alt width="589" height="715" referrerpolicy="no-referrer"></p>
<p>筛选后的结果如下所示（只显示了重复的数据，达到了我们的目的）：</p>
<p><img class="aligncenter size-full wp-image-57029" title="015" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/015.png" alt width="389" height="201" referrerpolicy="no-referrer"></p>
<h3 id="清除规则">2.4清除规则</h3>
<p>如果想恢复原来的数据，可以点击<strong>开始–>条件格式–>清除规则–>清除整个工作表的规则</strong>,清除掉该规则。</p>
<p><img class="aligncenter size-full wp-image-57030" title="016" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/016.png" alt width="1180" height="458" referrerpolicy="no-referrer"></p>
<h2 id="单元格内容拆分">3.单元格内容拆分</h2>
<p>一般情况下，开发在记录一些日志时，都会比较简单，如：1274206,商品1274206已淘汰，但是发给到运营时，运营一般都关注的比较细，需要明确的表头。</p>
<p>以下为程序中开发记录的日志：</p>
<p><img class="aligncenter size-full wp-image-57031" title="017" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/017.png" alt width="320" height="123" referrerpolicy="no-referrer"></p>
<p>但是发给运营时，运营需要明确的表头，如：商品编码，失败原因</p>
<p>此时就需要将单元格的内容根据,拆分成多个单元格，操作步骤如下：</p>
<h3 id="选中需要拆分的数据点击数据--分列">3.1.选中需要拆分的数据，点击数据–分列</h3>
<p><img class="aligncenter size-full wp-image-57032" title="018" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/018.png" alt width="932" height="273" referrerpolicy="no-referrer"></p>
<h3 id="选中单元框分隔符号点击下一步">3.2选中单元框：分隔符号，点击下一步</h3>
<p><img class="aligncenter size-full wp-image-57033" title="019" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/019.png" alt width="522" height="470" referrerpolicy="no-referrer"></p>
<h3 id="分隔符号选中逗号点击下一步然后点击完成">3.3分隔符号选中逗号，点击下一步，然后点击完成</h3>
<p><img class="aligncenter size-full wp-image-57034" title="020" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/020.png" alt width="512" height="468" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-57035" title="201" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/201.png" alt width="516" height="474" referrerpolicy="no-referrer"></p>
<p>此时会看到单元格的内容自动拆分成两列，如下所示：</p>
<p><img class="aligncenter size-full wp-image-57036" title="023" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/023.png" alt width="536" height="128" referrerpolicy="no-referrer"></p>
<h2 id="永久取消超链接">4.永久取消超链接</h2>
<p>在使用Excel的过程中，Excel会自动将网址转换为超链接，<strong>操作不当，容易误点</strong>，引起不必要的错误。</p>
<p>那么如何在Excel 2013里永久取消超链接呢？</p>
<p>1.依次打开菜单文件–选项，弹出Excel 选项弹出框</p>
<p>2.选中左侧菜单”校对”，点击”自动更正选项”</p>
<p>3.取消勾选”Internet 及网络路径替换为超链接”</p>
<p><img class="aligncenter size-full wp-image-57037" title="024" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/024.png" alt width="841" height="671" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-57038" title="025" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/04/025.png" alt width="474" height="454" referrerpolicy="no-referrer"></p>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            