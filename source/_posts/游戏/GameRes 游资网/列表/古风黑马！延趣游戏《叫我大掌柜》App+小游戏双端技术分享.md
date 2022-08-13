
---
title: '古风黑马！延趣游戏《叫我大掌柜》App+小游戏双端技术分享'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202208/12/110354znubii6i2bib14q9.png'
author: GameRes 游资网
comments: false
date: Fri, 12 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/12/110354znubii6i2bib14q9.png'
---

<div>   
由延趣游戏研发的古风模拟经营游戏《叫我大掌柜》上线至今已有一年多，在这段时间里，游戏不断充实内容、迭代优化，连宣发也在升级，成功吸引并留住了一大批玩家。在 Cocos Star Meetings 厦门站中，《叫我大掌柜》主程格兰和我们分享了该项目 App 和小游戏双端的技术开发经验。<br>
<br>
以下是分享实录：<br>
<br>
<div align="center">
<img aid="1049767" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110354znubii6i2bib14q9.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110354znubii6i2bib14q9.png" width="600" id="aimg_1049767" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110354znubii6i2bib14q9.png" referrerpolicy="no-referrer">
</div><br>
《叫我大掌柜》是一款面向全球发布的模拟经营游戏，目前已在8个国家或地区的多平台以多语言发布，所以也充分榨干了 git 的功能，做到内容版本快速更新迭代。<br>
<br>
项目立项时间是2019年中，当时只考虑发布 App，选择了比较新的 Cocos Creator 2.2.2 开发，UI系统编辑使用 fgui 来设计，主要看中其支持多语言多区域功能。<br>
<br>
小游戏版是在2021年4月投入研发，使用的是 Cocos Creator 2.4.4，后面升级到了 v2.4.7，跨度不大，升级比较简单。v2.4.x 开始支持 AssetBundle 功能，可以代替之前版本子包功能，性能更佳，也能更好地支持微信等小游戏的子包功能；另外升级也是考虑到对后面的 Creator 版本升级会更友好。<br>
<br>
<div align="center">
<img aid="1049766" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110354qrqmim1z4zeq2e7i.jpg" data-original="https://di.gameres.com/attachment/forum/202208/12/110354qrqmim1z4zeq2e7i.jpg" width="600" id="aimg_1049766" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110354qrqmim1z4zeq2e7i.jpg" referrerpolicy="no-referrer">
</div><br>
我们项目不希望玩家强制 App 强更，因为 App 强更可能会造成用户流失，所以该项目就不能进行 App 版本引擎升级，其中代码也无法做到分到各个子包中，导致代码只能放在一个子包里面，随着版本更新，代码量会越来越大，而当前项目子包只做资源管理更新。<br>
<br>
由于项目中存在两个 Cocos Creator 引擎版本，但是项目代码却只用一份， 所以我们也做了一套引擎 Api 兼容中间层，主要体现在资源加载管理和部分材质相关的代码。<br>
<br>
<div align="center">
<img aid="1049753" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110349mikfwhxse03pzh2f.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110349mikfwhxse03pzh2f.png" width="507" id="aimg_1049753" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110349mikfwhxse03pzh2f.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049755" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110350ldmmrmmodeje7imw.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110350ldmmrmmodeje7imw.png" width="148" id="aimg_1049755" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110350ldmmrmmodeje7imw.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049756" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110350a69bbjb9pvon7v9z.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110350a69bbjb9pvon7v9z.png" width="600" id="aimg_1049756" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110350a69bbjb9pvon7v9z.png" referrerpolicy="no-referrer">
</div><br>
本次我将分别介绍《叫我大掌柜》App 和小游戏两个版本的技术研发经验，抛砖引玉，供大家参考。<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">App 技术分享</font></font></strong><br>
<br>
<strong><font color="#de5650">多打包机打包</font></strong><br>
<br>
<strong><font color="#de5650">及热更、远程资源管理</font></strong><br>
<br>
如何高效打包热更包？针对这点，我们在 v2.2.2 的基础上进行了修改优化，若是较高版本的 Creator，可结合引擎热更逻辑判断以下几点是否可用。<br>
<br>
主要方案如下：<br>
<br>
更新超时时间不与更新文件数量关联，单个文件的超时时间也不与文件大小关联，而是整体超时体验可控、可配置。解决在热更过程中需要考虑到网络波动导致个别文件加载超时导致热更失败问题。<br>
<br>
修改版本对比逻辑，使热更可执行版本回退。引擎的热更只能对比高版本进行热更，但是在项目实践中有时需要让指定用户回退到指定热更版本。<br>
<br>
将所有资源划分为主包资源、子包资源、补充资源和远程资源四大类，扩充游戏后期内容的同时不增加初始下载包体大小，这个部分是常规操作，比较大型游戏大部分都会考虑到。<br>
<br>
通过对文件增加自定义 md5 校验,实现多台打包机交叉打包提高效率,避免不同打包机热更补丁大小异常。<br>
<br>
通过资源内容生成的 md5 来判断资源打包是否重新生成。<br>
<br>
注意：上面这两点是为解决不同机器或 meta 变化导致资源重新打包，但是实际上资源还是原来的没有改动，热更时会被判定为要热更该资源。<br>
<br>
<strong><font color="#de5650">表格数据加密和压缩</font></strong><br>
<br>
使用 npm 模块 xlsx 功能[1] 读取 excel 表格数据, 该模块 Api 比较稳定，便捷。<br>
<br>
表格数据使用 protobuf[2] 进行打包生成二进制内容文件，使用 protobuf 主要体现两点：生成文件小，加密高效。<br>
<br>
使用嵌入式 JS 模板引擎 EJS 定制 TS 文件内容：加载 protobuf 二进制文件代码,自定义枚举和结构体代码。<br>
<br>
把生成代码做成 JS 插件，在项目中添加该插件进行使用，使用插件可和项目代码进行解耦合。<br>
<br>
<strong><font color="#de5650">大地图显示和优化</font></strong><br>
<br>
可借鉴四叉树原理进行大地图分块加载，在这个项目中，我们也是根据项目需求自定义分块加载功能。<br>
<br>
滑动动态加载时是根据摄像机镜头属性判断进行加载。<br>
<br>
使用摄像机做移动、缩放、定位等视觉效果。<br>
<br>
注意：以上两点也是 Creator 推荐的方式，即尽量使用摄像机功能，而不是通过操作节点的属性去实现，可大大提高性能。<br>
<br>
判断摄像机显示范围控制大地图上物件显隐，不在指定范围内就不显示。<br>
<br>
<strong><font color="#de5650">2D 界面做 3D 景深效果</font></strong><br>
<br>
<div align="center">
<img aid="1049765" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110353jio6j6rjj5jibrv9.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/110353jio6j6rjj5jibrv9.gif" width="361" id="aimg_1049765" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110353jio6j6rjj5jibrv9.gif" referrerpolicy="no-referrer">
</div><br>
地板设置节点的 is3DNode 为 true，调整 eulerAngles 属性。<br>
<br>
旁边建筑图片设置 Texture2D 的 genMipmaps[3] 为 true，并进行纹理刷新才有效。<br>
<br>
关于 genMipmaps，为了加快 3D 场景渲染速度和减少图像锯齿而提高性能。<br>
<br>
<strong><font color="#de5650">Fgui 虚拟列表多层级节点使用</font></strong><br>
<br>
列表组件一直都是我们 UI 界面影响性能比较大并且最经常用到的组件，如果能够对列表进行深度优化，那将解决大部分 UI 界面性能问题。<br>
<br>
而 DrawCall 的渲染次数是一个重要衡量指标，该技术就是为解决渲染合批会被其他组件打断的问题。把一个列表分成多层级渲染，不会打断批次渲染的节点可以放在同一层，比如：图片节点（合图）一层，文本节点一层。<br>
<br>
若是 fgui 设计， 相关的 Api：GList.prototype.addLayer。<br>
<br>
<strong><font color="#ffffff"><font style="background-color:darkred">小游戏技术分享</font></font></strong><br>
<br>
<strong><font color="#de5650">小游戏启动流程优化</font></strong><br>
<br>
修改小游戏的 main.js 文件, 对里面下载流程添加异常判断并尝试重新下载和反馈信息给用户，这个是考虑到低网速引起的问题。<br>
<br>
把 RESOURCES 子包加载移出 main 逻辑流程，在启动页面再进行加载，提速启动。虽然资源是放在远程 cdn 上面，但是里面有一个 config.json 文件，我们项目资源非常多的，这个文件也是会有好几兆的大小，所有也需要对这个文件进行分批加载处理，避免低网速加载经常失败。<br>
<br>
删除项目中没有用到的引擎模块，这个是常规操作。<br>
<br>
使用小游戏独立分包来提速启动，但有些小游戏平台不支持，比如华为快游戏。<br>
<br>
多个文件可适当组合在一起，太大在低网速下载失败率高，太小则下载次数增加导致整体下载进度漫长。比如我们项目中表格配置文件就是分成多个组合文件下载，每一个组合文件大概 3M。<br>
<br>
<strong><font color="#de5650">Fgui 动态创建节点</font></strong><br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">和资源加载同步</font></strong><br>
<br>
常规界面打开逻辑流程是一个直线型流程：加载预制体，同时加载相应资源→创建节点→界面显示，处理业务逻辑。<br>
<br>
我们对这个流程进行了优化，用界面一点即开、内容逐一渲染的方式来展示界面。该技术设计核心是充分利用预制体配置文件和资源文件加载的耗时不同，而提前做了界面节点创建和业务逻辑处理。在小游戏平台上，这个方案的优化效果会更加明显，因为资源都是在远程 cdn，加载和网速紧密关联；而对低端机来说，复杂的界面中单单节点创建这个环节耗时就会更长。<br>
<br>
设计原理：<br>
<br>
加载界面 Fgui 包的 bin 文件（类似预制体配置）同时加载界面的图片资源合图。<br>
<br>
加载 bin 文件会比图片更快完成,然后创建界面节点，并记录纹理相关节点信息，在图片加载未完成之前也可以处理其他业务逻辑。<br>
<br>
等图片资源加载完成后，再重新设置界面纹理数据。<br>
<br>
纹理相关的节点包括：图片、帧动画、艺术字。<br>
<br>
<div align="center">
<img aid="1049863" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110936jggn944p3hp5zzdc.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110936jggn944p3hp5zzdc.png" width="600" id="aimg_1049863" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110936jggn944p3hp5zzdc.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">流程图</font></div><br>
当然界面快速打开也有涉及到其他方面知识，网上也有很多大神给出答案，比如界面资源合理规划并合图、分帧加载部分资源（spine 或特效）等。<br>
<br>
<strong><font color="#de5650">Fgui 虚拟列表分项加载</font></strong><br>
<br>
虚拟列表的意思是使用一屏或多一些的有限节点展示数量巨大的列表数据，节点重复使用而只是根据数据来刷新要展示的内容。比如用户上滑时，就将最底部的节点放置到最顶部，反之向下滑时就将最顶部的节点放置到最底部。<br>
<br>
<div align="center">
<img aid="1049758" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110351b9wqkwv9josvs7q9.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110351b9wqkwv9josvs7q9.png" width="516" id="aimg_1049758" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110351b9wqkwv9josvs7q9.png" referrerpolicy="no-referrer">
</div><br>
但是在小游戏环境下，受到网络和低配机影响，在同一帧创建展示一屏的节点内容，也会让用户在视觉上感受到卡顿，所以需要逐帧依次生成节点来提升界面效果。<br>
<br>
此外，支持不同节点来展示列表内容，底层根据当前所有节点大小和显示区域大小来判断是否创建或复用的节点，并设置节点位置。<br>
<br>
<div align="center"><font size="2">
<img aid="1049864" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110936d5i36ik665r1hr5b.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110936d5i36ik665r1hr5b.png" width="600" id="aimg_1049864" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110936d5i36ik665r1hr5b.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">流程图</font></div><br>
测试结果对比：<br>
<br>
<div align="center"><font size="2">
<img aid="1049752" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110349lanzb6ibilnxdahl.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/110349lanzb6ibilnxdahl.gif" width="484" id="aimg_1049752" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110349lanzb6ibilnxdahl.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">优化前</font></div><div align="center"><font size="2"><br>
</font></div><div align="center"><font size="2">
<img aid="1049754" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110350gqwxqtw86qxv8pwk.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/110350gqwxqtw86qxv8pwk.gif" width="484" id="aimg_1049754" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110350gqwxqtw86qxv8pwk.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">优化后</font></div><br>
<strong><font color="#de5650">小游戏代码压缩经验</font></strong><br>
<br>
小游戏有子包总量大小限制，比如，微信小游戏所有包体总量大小是不能超过 20M，主包不能超过 4M。但是前面说到 App 不能升级，项目通用一份代码，导致代码不能分包，只能放在一个子包里面，而且大小已经超过 20M。<br>
<br>
项目代码量大小的问题，只要建立在合理规划子包和业务逻辑的冗余程度控制基础上，一般项目是没什么太大问题，除非项目内容非常庞大而导致代码量超出限制。<br>
<br>
设计原理：<br>
<br>
使用 uglifyjs[4] 进行代码代码压缩，功能相对其他压缩方案更加优秀和稳定。<br>
<br>
修改 uglifyjs 生成简码是三位字符串开始,避免代码中三位以下字符串命名的冲突。<br>
<br>
需要配置跳过指定简码，比如：jsb。<br>
<br>
配置不生成简码命名，包括：<br>
<br>
网络通讯协议字段、表格字段，这两点原理上也可以做到代码压缩，但是考虑到影响面比较广，建议屏蔽；<br>
<br>
引擎特定字段（预制体属性，场景属性，shader 属性），不同平台适配代码的字段（微信小游戏）。这两点需要特别注意：如果是团队自行查找问题，需要对引擎代码和平台的适配文件逻辑非常清楚才能有把握解决问题，我们在实现过程中遇到过压缩后没有报错但是出现白屏或黑屏的问题，折腾了很久，后面也是在 Cocos 技术支持人员的帮助下修改正确，在此也向技术团队表示感谢！<br>
<br>
整合代码压缩流程为 Creator 插件并在打包流程执行。<br>
<br>
在小游戏和 H5 可起到加密代码的作用。<br>
<br>
代码需要定义简码和源码相互获取的接口，代码中有些逻辑必须使用到源码。<br>
<br>
<div align="center"><font size="2">
<img aid="1049865" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110936izmgnt9jjmr6g6g1.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110936izmgnt9jjmr6g6g1.png" width="600" id="aimg_1049865" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110936izmgnt9jjmr6g6g1.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">流程图</font></div><br>
我们对优化结果进行了测试，客户端编译后代码压缩率达到25%左右，最高我们游戏有测试过将 21.3M 压缩到 15.4M。<br>
<br>
另外有两个小 Tips，一是项目命名需要严格规范，需要注意通过""引用变量逻辑；二是推荐进行代码覆盖检测?[5]，可更全面地发现代码异常。<br>
<br>
<strong><font color="#de5650">代码文件分段下载优化方案</font></strong><br>
<br>
由于单个代码文件很大，在低网速情况下经常出现下载失败，微信小游戏子包下载是不支持断点续传的，而且是底层处理相应功能，我们是无法修改加载流程。<br>
<br>
Creator 的子包的 JS 代码内容主要是&#123;文件名：该 TS 文件内容&#125;，加载子包 JS 代码时会 require 里面每一个文件名。如下图：<br>
<br>
<div align="center">
<img aid="1049761" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110352uwqpeybwqim72f5m.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110352uwqpeybwqim72f5m.png" width="470" id="aimg_1049761" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110352uwqpeybwqim72f5m.png" referrerpolicy="no-referrer">
</div><br>
修改生成子包的 JS 文件内容加载流程:加载子包时只保存子包的 JS 文件内容&#123;文件名:该TS文件内容&#125;，不进行 require，也是对上面红框代码进行修改。<br>
<br>
把原来子包代码通过配置 TS 文件个数分隔成多个子包，相应的小游戏的子包配置也要修改，比如：setting.js,gam.json。<br>
<br>
<div align="center">
<img aid="1049762" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110352nhbm56p55v6p6hhj.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110352nhbm56p55v6p6hhj.png" width="600" id="aimg_1049762" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110352nhbm56p55v6p6hhj.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049763" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110352toa5pqot55vqxotz.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110352toa5pqot55vqxotz.png" width="600" id="aimg_1049763" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110352toa5pqot55vqxotz.png" referrerpolicy="no-referrer">
</div><br>
在游戏中加载相应的多个子包后再调用 require 保存文件名。<br>
<br>
<div align="center"><font size="2">
<img aid="1049866" zoomfile="https://di.gameres.com/attachment/forum/202208/12/110937tnnon3mbjw3b1wnr.png" data-original="https://di.gameres.com/attachment/forum/202208/12/110937tnnon3mbjw3b1wnr.png" width="600" id="aimg_1049866" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/110937tnnon3mbjw3b1wnr.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">流程图</font></div><br>
本次的分享就到这里，希望能对大家有所帮助，谢谢！<br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/5jeCCYfRWlEz--AYL5zgPQ</font><br>
<br>
<br>
  
</div>
            