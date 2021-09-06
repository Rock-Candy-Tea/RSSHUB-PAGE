
---
title: 'APP工具管理优化解析'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1222654-54102b5bef81aeb1.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1222654-54102b5bef81aeb1.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="480" data-height="320"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-54102b5bef81aeb1.png" data-original-width="480" data-original-height="320" data-original-format="image/png" data-original-filesize="31187" src="https://upload-images.jianshu.io/upload_images/1222654-54102b5bef81aeb1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><h1>一、背景<br>
</h1><p>本文中系列页面是面向内部工作人员的工具管理系统，目的是让工作人员快速、有效的找到应对不同角色工作的工具入口，具有多角色和多权限性。</p><p>该模块目前主要页面及核心流程图为：</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3273" data-height="1037"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-0ba3fcd09d1faf71.png" data-original-width="3273" data-original-height="1037" data-original-format="image/png" data-original-filesize="265914" src="https://upload-images.jianshu.io/upload_images/1222654-0ba3fcd09d1faf71.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><p><br></p><h1>二、目前存在的问题：</h1><h4>2.1、目前线上相同任务具有多个入口</h4><p>06页面我的工作下的更多按钮D点击进入05的更多工具页面，和07页面点击全部工具E显示的工具内容一致，只不过是排版不同的两个页面，做时的考虑初衷是为了多个入口能让用户方便些，但实际入口多时在用户心理形不成一个统一的认知路径，看到的页面不仅感觉内容多且不够效率，有学习成本。再一个开发需要实时维护两个相似的页面，增加开发成本。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1396" data-height="971"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-3636f45a56edb8dc.png" data-original-width="1396" data-original-height="971" data-original-format="image/png" data-original-filesize="128359" src="https://upload-images.jianshu.io/upload_images/1222654-3636f45a56edb8dc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h3><br></h3><h3>2.2、前后入口不一致、有理解成本</h3><p>有用户反馈，在页面01时（初始未添加常用工具），点击加号区域（A的位置）进行常用工具的添加，但之后在页面06时（有添加过常用工具），看到B的区域（无添加按钮），却不太清楚该如何进行常用工具的添加了。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1847" data-height="1037"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-022011e309f7aca0.png" data-original-width="1847" data-original-height="1037" data-original-format="image/png" data-original-filesize="136059" src="https://upload-images.jianshu.io/upload_images/1222654-022011e309f7aca0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h4><br></h4><h4>2.3、操作繁琐，任务路径较长</h4><p>有用户反馈，在页面01时，点击加号区域（A的位置）进行常用工具的添加，此时页面进入到页面02，但如果想进一步操作需要再次点击02页面上的A1加号区域，或右上角的编辑按钮C，才能进入编辑状态进行常用工具的添加、删除，感觉操作比较繁琐。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1365" data-height="923"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-e4832e6551cce356.png" data-original-width="1365" data-original-height="923" data-original-format="image/png" data-original-filesize="137698" src="https://upload-images.jianshu.io/upload_images/1222654-e4832e6551cce356.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><p><br></p><h1>三、优化方案1</h1><p>主要页面及核心流程图为：</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3273" data-height="1076"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-b4c42ad323ef318e.png" data-original-width="3273" data-original-height="1076" data-original-format="image/png" data-original-filesize="244200" src="https://upload-images.jianshu.io/upload_images/1222654-b4c42ad323ef318e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h4><br></h4><h4>3.1、改动较小，侧重工具管理、编辑</h4><p>点击页面01的加号区域A进入到02页面的编辑状态（原来03页面），点击06页面的更多按钮D进入更多工具04页面的编辑状态，等于是在用户想要添加常用工具的时候减少了一步操作。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1892" data-height="1076"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-0178f193851199d4.png" data-original-width="1892" data-original-height="1076" data-original-format="image/png" data-original-filesize="151953" src="https://upload-images.jianshu.io/upload_images/1222654-0178f193851199d4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h4>
<br>3.2、用户行为分析</h4><p>我们分析一下用户添加常用工具这个行为：不同角色和工具权限的的人员工作中经常用的工具可能就那么几个，这跟他的角色有很密切的关联关系，不会频繁的去添加删除常用工具，所以管理常用工具这个操作并不是一个频繁的操作。</p><p>当他想要点击更多按钮D进入到更多工具进行其他工具的查看时，还需要先取消编辑状态再点击相应的工具图标进入到详情，这种场景下操作会比较繁琐。</p><p>再一个更多工具页面里的F，是为了说明最多添加常用工具上限和目前添加了几个，但有的用户却误认为常用工具区域的图标可以左右滑，造成了一些理解成本。</p><p><br></p><h1>四、优化方案2<br>
</h1><p>根据上面的用户行为分析、思考，有了下面的优化方案：</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2831" data-height="1076"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-d584e0c37c60ae86.png" data-original-width="2831" data-original-height="1076" data-original-format="image/png" data-original-filesize="198216" src="https://upload-images.jianshu.io/upload_images/1222654-d584e0c37c60ae86.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h4><br></h4><h4>4.1、把上面我的工作、全部工具tab去掉</h4><p>可以放一些在此页面比较重要的其他信息，如用户头像，姓名等其他功能，增加用户专属感。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="483" data-height="871"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-012a3e51f5134062.png" data-original-width="483" data-original-height="871" data-original-format="image/png" data-original-filesize="29543" src="https://upload-images.jianshu.io/upload_images/1222654-012a3e51f5134062.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h4>
<br>4.2、添加按钮固定、统一<br>
</h4><p>01页面未添加常用工具时和06页面添加过常用工具后的添加按钮统一展示，统一用户心智模型（无论何时，都是点击此处进行常用工具的添加，减少理解成本）</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1865" data-height="980"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-954e135c6b3325e4.png" data-original-width="1865" data-original-height="980" data-original-format="image/png" data-original-filesize="138235" src="https://upload-images.jianshu.io/upload_images/1222654-954e135c6b3325e4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><p><br></p><h4>4.3、行为区分——查看更多工具场景</h4><p>01页面（未添加过常用工具）和06页面（添加过常用工具）的全部按钮（原来的更多按钮）一直存在，点击即进入03、04页面，如果用户从此处进入全部工具页面说明用户大概率想要查看其他工具的详情，即非编辑态，点击任一工具图标即可进入相应的详情页，此时如果用户想要进行常用工具的管理可以点击上面常用工具处的添加按钮进入工具编辑状态。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1856" data-height="965"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-5d62bcbfba85b6c5.png" data-original-width="1856" data-original-height="965" data-original-format="image/png" data-original-filesize="128077" src="https://upload-images.jianshu.io/upload_images/1222654-5d62bcbfba85b6c5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h4><br></h4><h4>4.4、行为区分——工具管理场景<br>
</h4><p>从01、06页面的添加按钮进入的全部工具页面的编辑状态即02、04页面，如果用户从此处进入全部工具页面说明用户大概率想要进行常用工具的管理；此时如果用户想要进入其他工具详情页面需要点击顶部导航左边的取消或右侧的保存（即退出编辑状态），然后点击点击任一工具图标即可进入相应的详情页，场景区分、入口减少统一、把用户认知统一化。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1861" data-height="1017"><img data-original-src="//upload-images.jianshu.io/upload_images/1222654-2440346a9f2aebf7.png" data-original-width="1861" data-original-height="1017" data-original-format="image/png" data-original-filesize="139669" src="https://upload-images.jianshu.io/upload_images/1222654-2440346a9f2aebf7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">点击查看大图</div>
</div><h1></h1><h1></h1><h1><b><br></b></h1><h1><b>五、思考总结：</b></h1><p>要通过不同的行为路径区分考虑用户的使用场景和行为动机，从而达到符合用户场景、方便用户行为的目的；而不要单方面的听从用户表面的问题表述，要尝试多角度的考虑问题背后的逻辑和其他的可能性，用户提出的问题有可能很主观也很片面，或者是单一场景下的单一问题，我们要做的是从大众用户心理出发，根据用户不同的使用场景进行综合考虑优化方案。</p>  
</div>
            