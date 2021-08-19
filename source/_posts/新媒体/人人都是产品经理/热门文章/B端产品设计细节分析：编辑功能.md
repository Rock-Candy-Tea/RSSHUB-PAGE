
---
title: 'B端产品设计细节分析：编辑功能'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/BUuLf0ynriSkIvS4qQir.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 15 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/BUuLf0ynriSkIvS4qQir.jpg'
---

<div>   
<blockquote><p>编辑导语：数据更新是B端产品的常见功能之一，而数据更新功能可以通过编辑功能实现。具体而言，B端产品中的编辑功能有哪些常见形式？本篇文章里，作者就编辑形式的种类、设计注意事项、如何应用等方面做了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5048891 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/BUuLf0ynriSkIvS4qQir.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、三种编辑形式</h2>
<p>一个B端产品的功能无外乎是新增（Create）、读取（Retrieve）、更新（Update）、删除（Delete）。数据更新可以通过编辑功能实现，常用于更新表单或列表数据，主要有以下三种形式：</p>
<ol>
<li>内联式编辑；</li>
<li>弹出式编辑；</li>
<li>跳转页面编辑。</li>
</ol>
<h3>1. 内联式编辑</h3>
<p>指在原页面编辑并保存的一种编辑形式。整个过程不会涉及到对话框的弹出和页面的跳转，用户清楚地知道编辑的内容会显示在哪里。</p>
<p>这有助于在不离开当前视图的情况下立即更改内容，防止用户丢失当前视图上下文的信息，常用于小范围内容更新。</p>
<p>内联多字段编辑一般有明显的编辑按钮，单一字段编辑时可以隐藏编辑按钮在鼠标悬浮时才出现，甚至没有编辑按钮，需要通过鼠标单击或双击进入编辑状态。</p>
<ul>
<li>优点：简单、直接，可方便用户联系上下文内容。</li>
<li>缺点：防错性较弱。</li>
<li>适用场景：常用于单一字段、重要性较弱的编辑。</li>
</ul>
<p><strong>1）基础样式</strong></p>
<p>用户触发某一栏时，该栏即变为可编辑状态。这时用户可以任意修改。并且当鼠标点击到其他栏或者表格以外的地方时，该可编辑栏失焦之后自动保存修改后的内容，并变回不可编辑状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dKdHT1huqEzYveZDJ7iA.png" alt width="763" height="450" referrerpolicy="no-referrer"></p>
<p>触发编辑的条件可以是单击或双击，但是为了使用户容易发现，大多数产品会添加编辑图标按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/caZuQE9kq6zHltFRTY3P.png" alt width="765" height="339" referrerpolicy="no-referrer"></p>
<p><strong>2）带按钮样式</strong></p>
<p>当鼠标悬浮到某一栏上时，出现编辑图标，点击图标出现「保存」 和 「取消」 按钮。编辑完成后点击「保存」即完成编辑，否则编辑内容不会被保存。</p>
<p>这种形式给用户适当的考虑时间，可以防止用户反悔或错误输入。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/y3gywUPNoa6U4EbPV7QP.png" alt width="763" height="388" referrerpolicy="no-referrer"></p>
<p><strong>3）行编辑/多个字段编辑</strong></p>
<p>与带按钮的编辑相似，点击编辑按钮时进入编辑状态，编辑完毕后可进行「保存」 或者 「取消」操作。</p>
<p>这种方式适合对列表同一行或表单的多个字段进行修改，且编辑字段内容较简单时使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DKpzNYtecQhTgYAXC3UV.png" alt width="765" height="451" referrerpolicy="no-referrer"></p>
<h3>2. 弹出式编辑</h3>
<p>指需要以弹框为载体进行编辑的形式。如果要编辑的字段较多，可使用这种方法。通常隐藏编辑按钮在鼠标悬浮时才出现。</p>
<p>弹窗编辑也包括三种形式：模态弹框形式、非模态弹框形式、以及模态抽屉形式。</p>
<ul>
<li>优点：可承载较多信息，防错性较强。</li>
<li>缺点：打破了用户的上下文连贯性，在保存后返回到之前的视图时，必须再次重新聚焦。</li>
<li>适用场景：用于复杂、较重要信息的编辑。</li>
</ul>
<p><strong>1）非模态弹框</strong></p>
<p>此类型的编辑仍停留在原页面，但是会有弹出框。弹出框不会遮盖需要更新的字段信息，并且弹出框悬停在编辑位置处。当用户点击弹出框以外的区域时，弹出框可消失。与模态弹框不同，这种弹出框不会阻断原页面和编辑内容的关联性。</p>
<p>这种方式适合修改较重要但又不复杂的信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ICoUWEv52pkSjDHCtNdZ.png" alt width="764" height="444" referrerpolicy="no-referrer"></p>
<p><strong>2）模态弹框</strong></p>
<p>这是常用的交互方式了。当鼠标悬浮要修改的字段时，出现编辑图标，点击图标会弹出可更新的字段内容弹框，并且原页面上会覆盖灰色透明蒙层，弱化原页面信息。操作结束后点击保存更新信息，否则信息不保存。</p>
<p>这种模式的好处是用户可以集中注意力在弹窗中内容，使用户谨慎操作，同时又不离开主页面。</p>
<p>这种方式适合修改重要但不太复杂的信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/OUPZyEfxG5Skb4K7HO9N.png" alt width="765" height="506" referrerpolicy="no-referrer"></p>
<p><strong>3）模态抽屉</strong></p>
<p>此类型与模态弹框类似，点击编辑后从左侧划入模态抽屉进行交互，用户可以更加专注于当前操作。</p>
<p>抽屉可以承载更多信息，可执行多步骤操作，常用于复杂的编辑功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8uNs5jzoq2NlPg1XVrqZ.png" alt width="764" height="553" referrerpolicy="no-referrer"></p>
<h3>3. 跳转页面编辑</h3>
<p>顾名思义，指点击编辑按钮或图标后跳转到新页面。用这种方式编辑记录时几乎没有限制，可以有大量文本内容，利用弹出框来设置字段值，放置验证消息等等。</p>
<p>常用于列表中，通常有明显的编辑按钮（操作栏），也会有鼠标悬浮时才出现的情况。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/v0MMKHQYbQNorOGJuVLp.png" alt width="763" height="275" referrerpolicy="no-referrer"></p>
<ul>
<li>优点：由于列表中会存在隐藏列，需要编辑的字段可能没有显示，这种形式可以看到之前填写记录的全部内容。</li>
<li>缺点：严重破坏了主页面信息的连贯性。</li>
<li>适用场景：编辑列表中的整条记录。</li>
</ul>
<p>跳转页面编辑样式与内联编辑、弹窗编辑有明显的区别，就不过多赘述了。需要注意的是，跳转页面后，不是所有信息都是可编辑的，不可编辑的需要置灰处理。</p>
<p>大多数企业级产品功能结构复杂，通常会使用内联与弹框、跳转页面相结合的形式。在这种情况下，允许编辑一些内联字段，其他字段在单独的页面或弹出框中编辑。</p>
<h2 id="toc-2">二、注意事项</h2>
<h3>1. 防错</h3>
<p>弹出式编辑的防错性要优于内联式编辑，使用弹窗意味着有更多的显示空间，这有助于：</p>
<p>1）显示帮助文本。</p>
<p>帮助文本可以提高用户的操作效率，可以是正在编辑的记录名称、编辑后带来的影响以及该如何操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oW6eNUp7fdXUMpm55HmG.png" alt width="762" height="385" referrerpolicy="no-referrer"></p>
<p>2）显示标题。标题可以提示用户所编辑的字段内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/4c5KiR3tjVylGuBf1Wgc.png" alt width="764" height="386" referrerpolicy="no-referrer"></p>
<p>3）以更清晰的方式呈现验证错误。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/m6GVQ9nPHc8QrPQuwR2N.png" alt width="762" height="358" referrerpolicy="no-referrer"></p>
<h3>2. 验证</h3>
<p>弹出式编辑的验证方式与表单相同，这种验证较常规，用户很好理解。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DlmLGZlZZ9Ov1lFMyPCR.png" alt width="761" height="331" referrerpolicy="no-referrer"></p>
<p>当您为用户提供内联式编辑时，报错会有些许不同，尤其是列表，没有多余的空间显示验证内容，可以考虑以下数据验证方法。</p>
<p>1）气泡提示</p>
<p>最简单的形式为气泡提示，帮助用户识别无效输入。当用户输入无效时会在编辑处附近弹出气泡显示帮助提示，解释错误及其解决方法。用户可以按照给定的信息在单元格中进行有效输入来消除错误。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/3Gwou94TnNZ45LI2VivE.png" alt width="763" height="314" referrerpolicy="no-referrer"></p>
<p>2）行下方提示</p>
<p>这种形式是在用户输入无效信息的行下方显示错误消息。使用此方法需要在表中受影响的行下方留出额外的空间。用户删除错误并输入正确内容后消失。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/jOisIWftmw7wN0GjcoEh.png" alt width="762" height="329" referrerpolicy="no-referrer"></p>
<p>3）通知提醒框</p>
<p>这种形式是在表格顶部显示错误消息。当用户输入无效信息时，错误消息将显示在顶部。受影响的单元格以红色显示，以便用户可以轻松识别错误并进行必要的更正。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/qfE4eldxYUxidVsLfDKl.png" alt width="763" height="333" referrerpolicy="no-referrer"></p>
<p>4）更改行颜色</p>
<p>还有一种选择是更改行的背景颜色以指示无效条目。错误的详细信息可以显示在当前视图的顶部，当用户解决错误时会隐藏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8Pr02df5LFEFcZpUgEL2.png" alt width="763" height="333" referrerpolicy="no-referrer"></p>
<h3>3. 模态</h3>
<p>对于是否使用模态通常会有不同的意见。有的人认为模态会打破页面视图的连贯性。但是如果将主屏幕和模态对话框构建为整个任务过程的共生部分，则不会感觉中断。</p>
<p>无论如何界面如何简单，所有复杂的操作都必须分解为步骤或模块。当列表中有一组具有复杂属性的对象时，弱化原页面的内容，将编辑图标按钮与编辑弹窗理解成一个整体，即是一个功能入口与功能界面的关系，此时模态会是最佳呈现方式。</p>
<p>只有当对象很简单并且所有属性都显示在列表中时，才可以使用非模态形式。因此，是否使用模态完全取决于对象的属性间的关系、产品的结构及用户的操作习惯。</p>
<h2 id="toc-3">三、如何选择</h2>
<h3>1. 功能是否复杂</h3>
<p>如果功能简单，尽量使用非模态的样式。</p>
<ul>
<li>编辑的字段重要性较低，选择内联编辑。</li>
<li>编辑的字段重要性较高，选择非模态弹出框的形式，方便放置验证信息。</li>
</ul>
<p>如果功能复杂，需要进行多步操作，可以使用模态形式。</p>
<ul>
<li>编辑内容步骤较少时，选择模态弹窗。</li>
<li>编辑内容步骤较多时，选择模态抽屉。</li>
</ul>
<h3>2. 是否批量编辑</h3>
<p>批量编辑使用模态的形式。批量编辑对于企业级产品很重要，这有助于让用户多选项目然后执行批量操作，在这种情况下非模态编辑十分有限。</p>
<p>由于编辑的内容会更改多条记录，需要用户谨慎操作，所以应该选择模态弹窗或抽屉形式。</p>
<h3>3. 是否有隐藏列</h3>
<p>若编辑列表的隐藏列内容，尽量使用新页面编辑。</p>
<p>使用内联式编辑和弹出式编辑，必须保证在列表中能查看到需要编辑的字段。如果产品允许用户隐藏列，或者只选择显示可编辑字段的子集，就必须使用能查看详细信息的视图了。</p>
<p>参考文章</p>
<ul>
<li>http://www.woshipm.com/pd/249837.html</li>
<li>https://ux.stackexchange.com/questions/53631/what-is-the-best-ux-to-let-user-perform-crud-operations</li>
<li>https://uxdworld.com/2020/04/22/inline-editing-and-validation-in-tables/</li>
</ul>
<p> </p>
<p>本文由 @LIZ酱 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5037613" data-author="1054439" data-avatar="http://image.woshipm.com/wp-files/2021/01/iH2zkLvy6O5tVZXjclsT.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            