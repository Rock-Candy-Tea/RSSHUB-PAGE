
---
title: 'C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/c8782c6b-4bdc-4555-9928-b9a601a94c71.gif'
author: IT 之家
comments: false
date: Fri, 19 Nov 2021 06:40:47 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/c8782c6b-4bdc-4555-9928-b9a601a94c71.gif'
---

<div>   
<p data-vmark="433d">你见过这样的超级马里奥吗？</p><p data-vmark="5b12">跑着跑着突然停下来个帅气掉头，“踩”扁“板栗仔”（goomba）时直接“变酷”（得到一副墨镜）：</p><p data-vmark="065e"><img src="https://img.ithome.com/newsuploadfiles/2021/11/c8782c6b-4bdc-4555-9928-b9a601a94c71.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="87ea">这，就是<span class="accentTextColor">一位油管博主用 C++ 和 SFML 自己从头制作的红白机版超级马里奥</span>。</p><p data-vmark="f814">C++ 不用介绍，SFML 想必有很多人也熟悉，就是一个用来简化写小游戏或者多媒体应用程序的 API，包括系统，窗口，图形，音频和网络五大模块。</p><p data-vmark="9844"><img src="https://img.ithome.com/newsuploadfiles/2021/11/ace29be4-424b-4b9e-8f8b-49d3b604f822.gif" w="1079" h="915" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1079" height="695" referrerpolicy="no-referrer"></p><p data-vmark="321a"><img src="https://img.ithome.com/newsuploadfiles/2021/11/9bc8323e-909f-45f5-968c-85c10513c78a.gif" w="728" h="682" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="728" height="682" referrerpolicy="no-referrer"></p><p data-vmark="d6cc">除了常规的功能和操作，你可以加入任何自己喜欢的元素。</p><p data-vmark="0bf0">由于画面看起来实在太逼真，有人甚至提醒博主：小心“版权狂魔”任天堂来找你哦！</p><p data-vmark="e7d8"><img src="https://img.ithome.com/newsuploadfiles/2021/11/18f4e05e-ddb2-42e9-bfb9-f1e5cb81dcfb.png" w="1024" h="168" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1024" height="135" referrerpolicy="no-referrer"></p><p data-vmark="cb5b">心动么？</p><p data-vmark="773c">你也可以自己做一个～</p><p data-vmark="febc">话不多说，来看教程。</p><h2 data-vmark="0453">手把手教你用 C++ 打造超级马里奥</h2><p data-vmark="0010">一共分为 4 大块。</p><p data-vmark="37dd"><strong>1、基本控制</strong></p><p data-vmark="a65a">设置游戏窗口大小为 256x240。</p><p data-vmark="b26c">我们先自己绘制一个留胡子的小伙子 —— 马里奥。</p><p data-vmark="3938"><img src="https://img.ithome.com/newsuploadfiles/2021/11/7f9e247b-d6f9-4c54-ac26-1e24be7e1948.png" w="1080" h="542" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="412" referrerpolicy="no-referrer"></p><p data-vmark="0e22">通过函数将它载入程序。</p><pre class="brush:javascript;toolbar:false">Mario::Mario() :
    x(0.5f * SCREEN_WIDTH),
    y(0.5f * SCREEN_HEIGHT)
&#123;
    texture.loadFromFile("Resources/Images/Mario.png");
    sprite.setTexture(texture);
&#125;
void Mario::draw(sf: :RenderWindow& i_window)
&#123;
    sprite.setPosition(round(x), round(y));
    i_window.draw(sprite);
&#125;</pre><p data-vmark="fadb">得到这样的界面：</p><p data-vmark="9e1d"><img src="https://img.ithome.com/newsuploadfiles/2021/11/c867ec67-9497-441c-ace7-1a38d3f585f2.png" w="730" h="728" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="730" height="728" referrerpolicy="no-referrer"></p><p data-vmark="d99f">然后处理地图，由于地图的宽度不同，将它存储为数组向量。</p><pre class="brush:javascript;toolbar:false ai-word-checked">typedef std::vector<std::array<Cel1, SCREEN_HEIGHT / CELL_SIZE>> Map;</pre><pre class="brush:javascript;toolbar:false">sf::Texture map_texture;
map_texture.1oadFromFile("Resources/Images/Map.png");
Map map(SCREEN_WIDTH/CELL_SIZE);
Mario mario;
for(unsigned short a = θ; a < map.size(); a++)
&#123;
    for (unsigned short b = map[a].size() - 2;b< map[a].size(); b++)
    &#123;
        map[a][b] = Cell: :Wa1l;
    &#123;
&#125;</pre><p data-vmark="9e42"><img src="https://img.ithome.com/newsuploadfiles/2021/11/86299a41-98c6-458b-bdaf-668e92aa46cc.png" w="1080" h="614" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="466" referrerpolicy="no-referrer"></p><p data-vmark="f1d7">现在画面是这样的：</p><p data-vmark="860e"><img src="https://img.ithome.com/newsuploadfiles/2021/11/167f1ec9-d6fb-4521-9e0b-83313eedd016.png" w="730" h="724" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="730" height="724" referrerpolicy="no-referrer"></p><p data-vmark="e388">接着开始集中打造马里奥。</p><p data-vmark="31a8">先让他能动起来，前进后退：</p><p data-vmark="679e"><img src="https://img.ithome.com/newsuploadfiles/2021/11/63078e57-d992-4015-8d17-f7b8ab882058.gif" w="728" h="728" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="728" height="728" referrerpolicy="no-referrer"></p><p data-vmark="8f95">并且获得重力：</p><pre class="brush:javascript;toolbar:false ai-word-checked">void Mario::update()
&#123;
    if (1 == sf::Keyboard: :isKeyPressed(sf: :Keyboard: :Left))
    &#123; 
        x-=MARIO_SPEED;
    &#125;
    else if (1 == sf::Keyboard::isKeyPressed(sf: :Keyboard: :Right))
    &#123;
        x+= MARIO_SPEED;
    &#125;
    vertical_speed += GRAVITY;
    y += vertical_speed;
&#125;</pre><p data-vmark="e48a"><img src="https://img.ithome.com/newsuploadfiles/2021/11/41d0af60-c309-4f41-8c0a-fdbf83f818c1.gif" w="728" h="728" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="728" height="728" referrerpolicy="no-referrer"></p><p data-vmark="1a0d">有了，但得让马里奥落到地上。</p><p data-vmark="56b5">那就获取一下马里奥的坐标，用下面这些公式检查与之相交的所有单元格：</p><p data-vmark="19b7"><img src="https://img.ithome.com/newsuploadfiles/2021/11/bcc4f398-5e40-414b-bd1a-753dfa7e5587.png" w="1080" h="553" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="420" referrerpolicy="no-referrer"></p><p data-vmark="0835">成功：</p><p data-vmark="a1ac"><img src="https://img.ithome.com/newsuploadfiles/2021/11/7331ad34-3658-4763-a6f9-df6dd61ee46e.gif" w="727" h="677" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="727" height="677" referrerpolicy="no-referrer"></p><p data-vmark="61d0">但是不能让马里奥跑出地图：</p><pre class="brush:javascript;toolbar:false">void Mario::update(const Map& i_map)
&#123;
    if (1 == sf::Keyboard::isKeyPressed(sf: :Keyboard: :Left))
    &#123; 
        x = std::max<float>(x - MARIO_SPEED,θ);
    &#125;
    else if (1 == sf::Keyboard: :isKeyPressed(sf: :Keyboard: :Right))
    &#123;
        x=std::min<float>(MARIO_SPEED + x,CELL_SIZE *(i_map.size() - 1));
    &#125;
&#125;</pre><p data-vmark="e256">接下来添加碰撞。</p><p data-vmark="9196">用二进制表示马里奥碰到的单元格，用一个地图碰撞函数检查并返回 0000-1111 这 15 种可能，然后使用位运算检查方向。</p><p data-vmark="be1c"><img src="https://img.ithome.com/newsuploadfiles/2021/11/a0aed683-1cf0-4c02-9849-e104326f7bcd.png" w="1080" h="565" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="429" referrerpolicy="no-referrer"></p><p data-vmark="cc5d"><img src="https://img.ithome.com/newsuploadfiles/2021/11/88979889-bcab-4b1c-a840-2c0b5a423193.gif" w="1079" h="689" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1079" height="524" referrerpolicy="no-referrer"></p><p data-vmark="68a3">成功：</p><p data-vmark="3a53"><img src="https://img.ithome.com/newsuploadfiles/2021/11/ca54ffca-bc68-4b4d-80d3-e6ac48c30522.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="96ba">接下来，看看它能不能跳过这个墙。</p><p data-vmark="ac0e"><img src="https://img.ithome.com/newsuploadfiles/2021/11/67c5d497-b2b7-4053-8f64-3d0974e346e3.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="2d2d">显然不行……</p><p data-vmark="db4a">搞起来，其中，为了使马里奥的跳跃高度和我们按住键盘的时长为正比，需要创建一个跳跃计时器变量。</p><pre class="brush:javascript;toolbar:false ai-word-checked">if (1 == sf: :Keyboard: :isKeyPressed(sf: :Keyboard: :Up))
&#123;
    if (θ == vertical_speed && θ < map_collision(x, 1 + y, Cell::Wa1l, i_map))
    &#123; 
        vertical_speed = MARIO_JUMP_SPEED;
        jump_timer = MARIO_JUMP_TIMER;
    &#125;
    else if (θ < jump_timer)
    &#123;
        vertical_speed = MARIO_JUMP_SPEED;
        jump_timer--;
    &#125;
    else
    &#123; 
        vertical_speed = std::min<float>(GRAVITY + vertical_speed, MAX_VERTICAL_SPEED);
    &#125;
&#125;</pre><p data-vmark="8cc8">再来挑战一下：</p><p data-vmark="7b47"><img src="https://img.ithome.com/newsuploadfiles/2021/11/d80e10ce-a252-4e33-9f97-4206e557ea0b.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="9ffb">完美。</p><p data-vmark="55f4">最后，给它添加加速度和摩擦力，也就是我们在文章一开头看到的那种刹车特效。</p><pre class="brush:javascript;toolbar:false">if (1 == sf::Keyboard: :isKeyPressed(sf: :Keyboard: :Left))
&#123;
    horizontal_speed=std::max(horizontal_speed-MARIO_ACCELERATION,-MARIO_WALK_SPEED);
&#125;
else if (1 == sf: :Keyboard::isKeyPressed(sf::Keyboard::Right))
&#123; 
    horizontal_speed =std::min(MARIO_ACCELERATION +horizontal_speed,MARIO_WALK_SPEED);
&#125;
else if (θ < horizontal_speed)
&#123; 
    horizontal_speed-=MARIO_ACCELERATION;
&#125;
else if (θ> horizontal_speed)
&#123; 
    horizontal_speed+=MARIO_ACCELERATION;
&#125;</pre><p data-vmark="741c">至此，基本控制就完成了，进入地图绘制部分。</p><p data-vmark="1ccf"><strong>2、地图</strong></p><p data-vmark="8ec2">将地图存为图片之前，需分为两部分，上部分存为砖块，下部分存为实体。</p><p data-vmark="c334"><img src="https://img.ithome.com/newsuploadfiles/2021/11/3a0f14d9-7388-4d58-899a-4d2c20dd8092.png" w="1080" h="545" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="414" referrerpolicy="no-referrer"></p><p data-vmark="f184">使用一个新函数将图像转为 map。</p><pre class="brush:javascript;toolbar:false ai-word-checked">Map convert_sketch(const sf::Image& i_map_sketch, Mario& i_mario)</pre><p data-vmark="4019">修改 drawback 函数获得砖块像素颜色，绘制砖块。再画点云朵，基础地图就好了。</p><p data-vmark="f965"><img src="https://img.ithome.com/newsuploadfiles/2021/11/1507c888-c111-4847-9268-d297b8a9fdbd.png" w="728" h="732" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="728" height="732" referrerpolicy="no-referrer"></p><p data-vmark="8339">接下来就是挨个绘制剩余元素了。</p><pre class="brush:javascript;toolbar:false">if (sf::Color(109,255,85)==pixel)//Flagpole
&#123;
    sprite_x=12;
    if (sf::Color(109,255,85) == pixel_up)
    &#123;
        sprite_y=1
    &#125;
&#125;</pre><p data-vmark="1506">成果如下：</p><p data-vmark="82c6"><img src="https://img.ithome.com/newsuploadfiles/2021/11/79e25ea4-c9e2-429e-bad5-3ac8990405aa.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="90ba"><img src="https://img.ithome.com/newsuploadfiles/2021/11/f2ca028a-7f4c-4f7e-80bb-174d4d2ca99c.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="2e9e">什么？缺个城堡？作者表示：累了，随便吧……</p><p data-vmark="90b3">接下来，使用下面这个公式，让界面跟着马里奥前进后退。</p><pre class="brush:javascript;toolbar:false ai-word-checked">short view_x = std::clamp<int>(mario.get_x()+0.5f *(CELL_SIZE - SCREEN_WIDTH),θ,CELL_SIZE*n)</pre><p data-vmark="f4fb"><img src="https://img.ithome.com/newsuploadfiles/2021/11/d40f26b6-81c3-4218-ad3e-eafeb5701295.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="64d3">地图搞定，上板栗仔！</p><p data-vmark="f733"><strong>3、板栗仔</strong></p><p data-vmark="f512">板栗仔的行动和马里奥相似，代码可以基本复制。不同的是一旦它们碰到东西就会改变方向。</p><p data-vmark="6780">如何让板栗仔出现？</p><p data-vmark="62e9"><img src="https://img.ithome.com/newsuploadfiles/2021/11/4580fe9d-b6e5-4872-8368-d180693bd672.png" w="516" h="616" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="516" height="616" referrerpolicy="no-referrer"></p><p data-vmark="81bc">当马里奥靠近它们时，更新地图。</p><pre class="brush:javascript;toolbar:false">void Goomba::draw(unsigned 1_view_x, sf::RenderWindow& i_window)
&#123;
    if (-CELL_SIZE < round(y) && round(x) > static_cast<int>(i_view_x) - CELL_SIZE && round(x)
    &#123;
        sprite.setTexture(texture);
        sprite.setPosition(round(x),round(y));
        i_window.draw(sprite);
    &#125;
&#125;</pre><p data-vmark="f8e1"><img src="https://img.ithome.com/newsuploadfiles/2021/11/195b0527-187a-4bdc-aa66-72552e066bf1.png" w="1080" h="615" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="467" referrerpolicy="no-referrer"></p><p data-vmark="4d8b">然后在这部分加上板栗仔和马里奥的的死亡函数，包括两个条件，一是当马里奥跳到板栗仔头上，板栗仔挂；二是当马里奥碰到板栗仔后，马里奥挂。</p><pre class="brush:javascript;toolbar:false ai-word-checked">if(0 ==death_timer)
&#123;
    vertical_speed =std::min(GRAVITY + vertical_speed, MAX_VERTICAL_SPEED);
    y+= vertical_speed;
&#125;
else if (1 == death_timer)
&#123;
    vertical_speed = MARIO_JUMP_SPEED;
&#125;
death_timer = std::max(0, death_timer - 1);</pre><p data-vmark="830c">经历过 n 个 bug 后，终于没问题。</p><p data-vmark="90d5"><img src="https://img.ithome.com/newsuploadfiles/2021/11/21979030-d02d-402d-8001-d18f909bd1a0.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="413e">到了最后一部分了。</p><p data-vmark="f3c0"><strong>4、优化</strong></p><p data-vmark="3387">这部分主要就是做做代码优化，根据自己喜好改变一些原作风格什么的。</p><p data-vmark="9b4a">比如重新绘制一个马里奥，并分成三种状态：暂停、行走、跳跃以及 die。</p><p data-vmark="41aa"><img src="https://img.ithome.com/newsuploadfiles/2021/11/d922696c-8aca-47e3-9a47-e6bbcd6d7cb2.jpg@s_2,w_820,h_532" w="1080" h="701" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" srcset="https://img.ithome.com/newsuploadfiles/2021/11/d922696c-8aca-47e3-9a47-e6bbcd6d7cb2.jpg 2x" width="1080" height="532" referrerpolicy="no-referrer"></p><p data-vmark="cae9">还有玩家突然切换前进方向时的俏皮动作：</p><p data-vmark="b1d5"><img src="https://img.ithome.com/newsuploadfiles/2021/11/4729e535-404f-4064-b42b-930eedb0fd27.png" w="1080" h="350" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="266" referrerpolicy="no-referrer"></p><p data-vmark="125c">写一个切换状态函数进行控制。</p><pre class="brush:javascript;toolbar:false">void Animation::update()
&#123;
    animation_iterator++;
    while (animation_iterator >= animation_speed)
    &#123;
        animation_iterator -= animation_speed;
        current_frame = (1 + current_frame)% total_frames;
    &#125;
&#125;</pre><p data-vmark="eeda">终于，全部搞定！！</p><p data-vmark="9bf0"><img src="https://img.ithome.com/newsuploadfiles/2021/11/585e79c6-85f5-4807-b5bb-f6b819451bdd.gif" w="712" h="718" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="712" height="718" referrerpolicy="no-referrer"></p><p data-vmark="2bd3">怎么样？还挺成功吧？</p><p data-vmark="363d">过程其实也不乏挑战，有网友就表示：我以为很简单，直到我看到了代码。</p><p data-vmark="bb31"><img src="https://img.ithome.com/newsuploadfiles/2021/11/ad782372-e457-4b6c-a8c1-88670845f077.png" w="1080" h="138" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="105" referrerpolicy="no-referrer"></p><p data-vmark="ef4c">而现在你是不是也对背后的作者产生了一丝好奇？</p><p data-vmark="fd5e">下面就来认识一下。</p><h2 data-vmark="b658">作者介绍</h2><p data-vmark="3e2c">这位博主叫 Kofybrek，今年 6 月刚刚成为一名 YouTuber，目前已有 1000 粉丝。</p><p data-vmark="b300"><img src="https://img.ithome.com/newsuploadfiles/2021/11/b46b30e1-bced-4517-b2d5-87e1c9fe4a59.png" w="1080" h="435" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="330" referrerpolicy="no-referrer"></p><p data-vmark="0b12">他用 C++ 做了很多小游戏：包括扫雷、俄罗斯方块、吃豆人等等。</p><p data-vmark="7e29">也搞机器学习，比如教 AI 玩 Flappy Bird。</p><p data-vmark="81d8"><img src="https://img.ithome.com/newsuploadfiles/2021/11/c80c3cc3-55db-42c0-97e0-91e5281d2530.png" w="1080" h="470" title="C++ 从零打造《超级马里奥》：会漂移掉头，还带刹车音效" width="1080" height="357" referrerpolicy="no-referrer"></p><p data-vmark="6d0a">从他的座右铭“I do programming for fun”，可以看出小哥是很喜欢用编程做一些好玩的东西了，可以期待他更多的作品。</p><p data-vmark="6d4a">最后，如果你想试试亲手打造这样一个马里奥，可以戳下面的链接。</p><p data-vmark="3fee"><strong>代码：</strong></p><p data-vmark="19ea"><span class="link-text-start-with-http">https://github.com/Kofybrek/Super-Mario-Bros</span></p>
          
</div>
            