
---
title: 'Roguelike玩法的《少女前线：云图计划》，如何引发二次元玩家狂欢？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202201/17/165528fwpuzksbz27iwxi7.jpg'
author: GameRes 游资网
comments: false
date: Invalid Date
thumbnail: 'https://di.gameres.com/attachment/forum/202201/17/165528fwpuzksbz27iwxi7.jpg'
---

<div>   
2021 年 9 月，由散爆网络开发的《少女前线：云图计划》正式上线，随即引发了一场二次元游戏玩家的狂欢。作为《少女前线》IP 系列首部与玩家见面的新作，该作在上线前的全网预约数就超过了 200 万，正式上线后的战绩更是不负大家所望，上线当日下载量突破百万，荣获苹果 App Store Today 推荐，上线次日游戏免费榜登顶首位。<br>
<br>
<div align="center">
<img aid="1028336" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165528fwpuzksbz27iwxi7.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165528fwpuzksbz27iwxi7.jpg" width="600" id="aimg_1028336" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165528fwpuzksbz27iwxi7.jpg" referrerpolicy="no-referrer">
</div><br>
《少女前线：云图计划》采用了 Roguelike 的玩法，让刺激爽快的打斗和长线养成玩法两两结合。精美的画风、流畅的游戏体验，都成为了它突破重围的亮点所在。本次，Unity 采访了《少女前线：云图计划》的主创团队，听他们聊一聊这款游戏的开发故事。<br>
<br>
<strong>能和大家介绍下《少女前线:云图计划》和《少女前线》之间存在着怎样的联系吗？</strong><br>
<br>
本作是以美少女角色和军事题材闻名的《少女前线》衍生出的“少女前线宇宙”系列中，第一部和玩家们见面的作品，使用了和前者一致的世界观。<br>
<br>
故事开始于 2060 年，由于旨在备份“人形”们心智数据的“心智云图”计划发生了事故，参与测试的人形心智全部失联，并迷失在云端“麦戈拉”的各个扇区当中。三年后，在帕斯卡博士的帮助下，玩家借用云图计划负责人“教授”的权限，上传至云端寻找失联的人形心智和失踪的“教授”本人，并且和云端中的安全程序“净化者”以及神秘的敌人“熵”周旋，以保护人形心智的家园“绿洲”，并发掘云图计划当年事故背后的种种秘密。<br>
<br>
<div align="center">
<img aid="1028337" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165528yxxsgeys00j325f0.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165528yxxsgeys00j325f0.jpg" width="600" id="aimg_1028337" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165528yxxsgeys00j325f0.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>《少女前线：云图计划》的美术表现圈粉很多，这方面是否有什么设计与优化心得跟大家分享一下呢?</strong><br>
<br>
游戏中会有很多带轻微旋转的 UI 窗体，正常情况下，为了合批把每一个组件拆分出来，但是这样开发会很麻烦。最后方案就是在 UI 的 Shader 中添加一个 float4x4 的 uniform 属性，然后将设置好的旋转的矩阵传入 UI 的 Shader 中，UI 的 Transform 上不设置旋转值，由一个脚本组件来给需要旋转 UI 的 Material 传入渲染矩阵。<br>
<br>
<div align="center">
<img aid="1028338" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165529qkcgzklc6lk89qcy.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165529qkcgzklc6lk89qcy.jpg" width="600" id="aimg_1028338" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165529qkcgzklc6lk89qcy.jpg" referrerpolicy="no-referrer">
</div><br>
角色在制作的时候，会做出高中低三种。脸和身体分成两个 mesh，高模共 1.3w 面带 Blend Shape 脸部表情，中模共 8-9k 面用高模的脸部带表情，身体精简。低模共 7k 面，用中模的精简身体，脸部也精简不带表情。<br>
<br>
<div align="center">
<img aid="1028339" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165529vfe2boj4w6kwiszf.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165529vfe2boj4w6kwiszf.jpg" width="600" id="aimg_1028339" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165529vfe2boj4w6kwiszf.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>能否和大家分享一下使用 Burst 编译的开发经验？</strong><br>
<br>
Burst 主要在第三方的动态骨骼上运用。牵扯到大量物理运算时会用到很多的矢量和结构体，只要要做好数据的读写分离，使用 ReadOnly WriteOnly 属性标记。使用 [BurstCompile] 属性就可以非常方便的获得性能提升。<br>
<br>
<strong>《少女前线：云图计划》在机型适配方面有什么经验呢？</strong><br>
<br>
初代 metal1 对 alpha 值预乘会导致 (0,0,0,1) 变成 (0,0,0)。在旧型号 iOS 设备上如 ipadmini 和 iphone6 会让透明贴图出现白斑或黑斑，需要处理透明度为 0 的情况。<br>
<br>
<div align="center">
<img aid="1028340" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165529h66y3638byql8l0j.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165529h66y3638byql8l0j.jpg" width="600" id="aimg_1028340" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165529h66y3638byql8l0j.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>很多粉丝都在关注的一个问题, 未来是否还会有其他少前系列的作品问世？</strong><br>
<br>
2019 年，散爆公布了多款与《少女前线》处在同一世界观下，玩法不同的新作。其中 2021 年 9 月已经公测上线的《少女前线：云图计划》是《少女前线》IP 系列首部与玩家见面的新作，其他几部作品也在研发中，后续将会陆续与玩家见面。<br>
<br>
<div align="center">
<img aid="1028341" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165530bvwvgve0wz2n6e21.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165530bvwvgve0wz2n6e21.jpg" width="600" id="aimg_1028341" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165530bvwvgve0wz2n6e21.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>最后, 跟大家介绍一下咱们的团队吧？</strong><br>
<br>
《少女前线：云图计划》研发团队约 50 人规模，团队组成除《少女前线》初创核心成员外，还包含来自国内各大知名游戏厂商的骨干成员，游戏项目经验丰富。<br>
<br>
<div align="center">
<img aid="1028342" zoomfile="https://di.gameres.com/attachment/forum/202201/17/165531ucxcecv62c2vchht.jpg" data-original="https://di.gameres.com/attachment/forum/202201/17/165531ucxcecv62c2vchht.jpg" width="600" id="aimg_1028342" inpost="1" src="https://di.gameres.com/attachment/forum/202201/17/165531ucxcecv62c2vchht.jpg" referrerpolicy="no-referrer">
</div><br>
《少女前线：云图计划》研发团队所属的散爆网络科技有限公司旗下主要作品为二次元枪娘养成战术手游《少女前线》，该游戏产品已登陆海内外市场并取得优秀的成绩：2016 年 5 月在 App Store 正式上线；2018 年 1 月获得韩国游戏畅销榜第 1 名；同年 8 月获得日本游戏免费排行榜第 1 名；2021 年全球累计下载总量达到 1340 万。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/3BkGCjArOF4Lyy-jK8iBJQ</font></font><br>
<br>
  
</div>
            