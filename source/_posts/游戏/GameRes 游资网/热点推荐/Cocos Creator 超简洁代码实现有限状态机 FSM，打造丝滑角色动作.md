
---
title: 'Cocos Creator 超简洁代码实现有限状态机 FSM，打造丝滑角色动作'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202202/16/112913fccidnddw37plu7w.gif'
author: GameRes 游资网
comments: false
date: Wed, 16 Feb 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202202/16/112913fccidnddw37plu7w.gif'
---

<div>   
引言：本文作者黄聪是一名在校大学生，设计毕设的过程中，他参考《游戏编程模式》一书，摸索出了一套角色动作控制方案。<br>
<br>
作为一名在校学生，前段时间在做毕业设计的过程中，我也遇到了很多同学都会遇到的问题：角色的动作逻辑全都写在 Player.ts 里面，当一个玩家脚本需要同时执行多个逻辑的时候（移动控制，动画播放，按键管理等等），无一例外地出现了这样的局面——<br>
<br>
我们优雅地判断了按键输入，希望在 WASD 的按键驱动下，让我们的主人公顺理成章地旋转跳跃翻飞升华，于是在判断按键输入的代码块里改变了角色的动作播放，又设置了移动速度，还在某个 update 里面不停地设置他的方向……<br>
<br>
光是想想我就已经戴上了痛苦面具！于是我在网上搜索了各路资料，在不懈的努力下最终摸索出了一套方案，思路基于游戏编程模式中的状态模式（State Pattern）。<br>
<br>
以下是我在 Cocos Creaotr 2.4.x 用框架实现的角色移动、跳跃、下蹲、跳斩状态之间的切换效果，且 Player.ts 脚本内不再包含状态的行为逻辑。<br>
<br>
<div align="center"><font size="2">
<img aid="1030901" zoomfile="https://di.gameres.com/attachment/forum/202202/16/112913fccidnddw37plu7w.gif" data-original="https://di.gameres.com/attachment/forum/202202/16/112913fccidnddw37plu7w.gif" width="600" id="aimg_1030901" inpost="1" src="https://di.gameres.com/attachment/forum/202202/16/112913fccidnddw37plu7w.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">成品效果，部分素材来源于网络</font></div><br>
<strong><font color="#de5650">初试</font></strong><br>
<br>
让我们从零开始。为了保证思路清晰，我们假设现在在做一个 2D 横版闯关游戏，需要让主角对我们的键盘输入做出响应，按下空格键跳跃。这个功能看起来很容易实现：<br>
<br>
Player.ts<br>
<br>
private _jumpVelocity: number = 100;<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
if (cc.macro.KEY.space == event.keyCode) &#123;<br>
<br>
this.node.getComponent(Rigibody).setVerticalVelocity(this._jumpVelocity);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
但这有个问题，没有东西可以阻止「空中跳跃」，当角色在空中时疯狂按下空格，角色就会浮空。简单的修复方式是给 Player.ts 增加一个 _onGround 字段，然后这样：<br>
<br>
private _onGround: boolena = false;<br>
<br>
private _jumpVelocity: number = 100;<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
if (cc.macro.KEY.space == event.keyCode) &#123;<br>
<br>
if(this._onGround) &#123;<br>
<br>
this._onGround = false;<br>
<br>
// 跳跃...<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
意识到了吗？此时我们还没有实现角色的其他动作。当角色在地面上时，我希望按下↓方向键时，角色能够卧倒，松开时又能站起来：<br>
<br>
private _onGround: boolena = false;<br>
<br>
private _jumpVelocity: number = 100;<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
if (cc.macro.KEY.space == event.keyCode) &#123;<br>
<br>
if(this._onGround) &#123;<br>
<br>
this._onGround = false;<br>
<br>
// 如果在地上，就跳起来<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
else if (cc.macro.KEY.down == event.keyCode) &#123;<br>
<br>
if (this._onGround)&#123;<br>
<br>
// 如果在地上，就卧倒<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
onKeyUp(event: any) &#123;<br>
<br>
if (cc.macro.KEY.down == event.keyCode) &#123;<br>
<br>
// 起立<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
新的问题出现了。通过这段代码，角色可能从卧倒状态跳起来，并且可以在空中按方向键趴下，这可不是我们想要的，因此这时候又要加入新的字段……<br>
<br>
private _onGround: boolena = false;<br>
<br>
private _isDucking: boolean = false;<br>
<br>
private _jumpVelocity: number = 100;<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
if (cc.macro.KEY.space == event.keyCode) &#123;<br>
<br>
if(this._onGround && !this._isDucking) &#123;<br>
<br>
this._onGround = false;<br>
<br>
// 如果在地上，不在卧倒，就跳起来<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
else if (cc.macro.KEY.down == event.keyCode) &#123;<br>
<br>
if (this._onGround)&#123;<br>
<br>
this._isDucking = true;<br>
<br>
// 如果在地上，就卧倒<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
onKeyUp(event: any) &#123;<br>
<br>
if (cc.macro.KEY.down == event.keyCode) &#123;<br>
<br>
if (this._isDucking) &#123;<br>
<br>
this._isDucking = false;<br>
<br>
// 起立<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
但是这样的实现方法很明显有很大问题。每次我们改动代码时，就会破坏之前写好的一些东西。我们需要增加更多动作——滑铲、跳斩攻击、向后闪避等，但若用这种方法，完成之前就会造成一堆漏洞。<br>
<br>
<strong><font color="#de5650">有限状态机(FSM)</font></strong><br>
<br>
经历了上述的挫败后，我痛定思痛，把桌面清空，留下纸笔，开始画流程图。我给角色的每个行为都画了一个盒子：站立、跳跃、卧倒、跳斩……当角色响应按键时，画一个箭头，连接到它需要切换的状态。<br>
<br>
<div align="center">
<img aid="1030902" zoomfile="https://di.gameres.com/attachment/forum/202202/16/112913vr3l86wwv3vvzwrl.jpg" data-original="https://di.gameres.com/attachment/forum/202202/16/112913vr3l86wwv3vvzwrl.jpg" width="600" id="aimg_1030902" inpost="1" src="https://di.gameres.com/attachment/forum/202202/16/112913vr3l86wwv3vvzwrl.jpg" referrerpolicy="no-referrer">
</div><br>
如此，就建立好了一个有限状态机，它的特点是：<br>
<br>
拥有角色所有可能状态的集合。在这里，状态有站立、卧倒、跳跃以及跳斩。<br>
<br>
状态机同一时间只能处于一个状态。角色不可能同时处于站立和卧倒状态，这也是使用 FSM 的理由之一。<br>
<br>
所有的按键输入都将发送给状态机。在这里就是不同按键的按下和弹起。<br>
<br>
每个状态都有一系列的状态转移、转移条件和输入与另一个状态相关。当处于这个状态下，输入满足另一个状态的条件，状态机的状态就切换到目标的状态。<br>
<br>
<strong>这就是状态机的核心思维：状态、输入、转移。</strong><br>
<br>
<strong><font color="#de5650">枚举与分支</font></strong><br>
<br>
回来分析之前的代码存在的问题。首先，它不合时宜地捆绑了一大堆 bool 变量：_onGround 和 _isDucking 这些变量似乎不可能同时为真或假，因此我们需要的其实是枚举。类似这样：<br>
<br>
enum State &#123;<br>
<br>
STATE_IDLE,<br>
<br>
STATE_JUMPING,<br>
<br>
STATE_DUCKING,<br>
<br>
STATE_DIVING<br>
<br>
&#125;;<br>
<br>
这样一来不需要一堆字段，我们只需要根据枚举进行对应的判断：<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
switch(_state) &#123;<br>
<br>
case State.STATE_IDLE:<br>
<br>
if(cc.macro.KEY.space == event.keyCode)&#123;<br>
<br>
_state = STATE_JUMPING;<br>
<br>
// 跳跃...<br>
<br>
&#125;<br>
<br>
else if (cc.macro.KEY.down == event.keyCode) &#123;<br>
<br>
_state = STATE_DUCKING;<br>
<br>
// 卧倒...<br>
<br>
&#125;<br>
<br>
break;<br>
<br>
case State.STATE_JUMPING:<br>
<br>
if (cc.macro.KEY.down == event.keyCode) &#123;<br>
<br>
_state = STATE_DIVING;<br>
<br>
// 跳斩...<br>
<br>
&#125;<br>
<br>
break;<br>
<br>
case State.STATE_DUCKING:<br>
<br>
//...<br>
<br>
break;<br>
<br>
&#125;<br>
<br>
看起来也就改变了一点点，但是比起之前的代码有了很大的进步。我们在条件分支进行了区分，将某个状态中运行的逻辑聚合到了一起。<br>
<br>
这是最简单的状态机实现方式，但是实际问题没有这么简单。我们的角色还存在着按键蓄力，松开时进行一段特殊攻击。现在的代码没有办法很清晰地胜任这样的工作。<br>
<br>
还记得一开始画的状态机流程图吗？每一个状态方盒子给了我一些灵感，于是我开始尝试，用面向对象的思想去设计状态机。<br>
<br>
<strong><font color="#de5650">状态模式</font></strong><br>
<br>
即使 switch 可以完成这些需求，但就像我们用起来的那样：崎岖且繁琐。因此我决定去使用游戏编程模式中的思想，让我们能使用简单的接口去完成复杂的逻辑工作，目标还是老样子：高内聚，低耦合。<br>
<br>
<strong>状态接口</strong><br>
<br>
将状态封装成一个基类，用于控制某个状态相关的行为，并让状态记住自己所依附的角色信息。<br>
<br>
这么做的目的很明确：让每个状态拥有相同的类型与共性，方便我们集中管理。<br>
<br>
/**状态基类，提供状态的逻辑接口 */<br>
<br>
export default class StateBase &#123;<br>
<br>
protected _role: Player | null = null;<br>
<br>
constructor(player: Player) &#123;<br>
<br>
this._role = player;<br>
<br>
&#125;<br>
<br>
//start------------虚方法-----------<br>
<br>
/**进入该状态时被调用 */<br>
<br>
onEnter() &#123; &#125;<br>
<br>
/**该状态每帧都会调用的方法 */<br>
<br>
onUpdate(dt: any) &#123; &#125;<br>
<br>
/**该状态监听的键盘输入事件 */<br>
<br>
onKeyDown(event: any) &#123; &#125;<br>
<br>
/**该状态监听的键盘弹起事件 */<br>
<br>
onKeyUp(event: any) &#123; &#125;<br>
<br>
/**离开该状态时调用 */<br>
<br>
onExit() &#123; &#125;<br>
<br>
//end--------------虚方法------------<br>
<br>
&#125;<br>
<br>
<strong><font color="#000000">为每个状态写一个类</font></strong><br>
<br>
对于每个状态，我们定义一个类的实现接口。<br>
<br>
它的方法定义了角色在这个状态的行为。换句话说，从之前的 switch 中取出每个 case，将它们移动到状态类中。<br>
<br>
export default class Player_Idle extends StateBase &#123;<br>
<br>
onEnter(): void &#123; &#125;<br>
<br>
onExit(): void &#123; &#125;<br>
<br>
onUpdate(dt: any): void &#123; &#125;<br>
<br>
onKeyDown(event: any): void &#123;<br>
<br>
switch (event.keyCode) &#123;<br>
<br>
case cc.macro.KEY.space:<br>
<br>
// 跳跃状态<br>
<br>
break;<br>
<br>
case cc.macro.KEY.down:<br>
<br>
// 卧倒状态<br>
<br>
break;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
onKeyUp(event: any): void &#123; &#125;<br>
<br>
&#125;<br>
<br>
要注意，这里就已经把原本写在 Player.ts 中的 Idle 状态逻辑移除，放到了 Player_Idle.ts 类中。这样非常的清晰——在这个状态内只存在我们需要他判断的逻辑。<br>
<br>
<div align="center">
<img aid="1030903" zoomfile="https://di.gameres.com/attachment/forum/202202/16/112914czo2a9x8hud8s7z7.jpg" data-original="https://di.gameres.com/attachment/forum/202202/16/112914czo2a9x8hud8s7z7.jpg" width="220" id="aimg_1030903" inpost="1" src="https://di.gameres.com/attachment/forum/202202/16/112914czo2a9x8hud8s7z7.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>状态委托</strong><br>
<br>
接下来，重新构建角色内原来的逻辑，放弃庞大的 switch，通过一个变量来存储当前正在执行的状态。<br>
<br>
export default class Player &#123;<br>
<br>
protected _state: StateBase | null = null; //角色当前状态<br>
<br>
constructor() &#123;<br>
<br>
onInit();<br>
<br>
&#125;<br>
<br>
onInit() &#123;<br>
<br>
this.schedule(this.onUpdate);<br>
<br>
&#125;<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
this._state.onKeyDown(event);<br>
<br>
&#125;<br>
<br>
onKeyUp(event: any) &#123;<br>
<br>
this._state.onKeyUp(event);<br>
<br>
&#125;<br>
<br>
onUpdate(dt) &#123;<br>
<br>
this._state.onUpdate(dt);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
为了「改变状态」，我们只需要将 _state 指向不同的 StateBase 对象，这样就实现了状态模式的全部内容。<br>
<br>
<strong>将状态存在哪里？</strong><br>
<br>
又一个小细节：上面说到，为了「改变状态」，我们需要将 _state 指向新的状态对象，但是这个对象从哪里来呢？<br>
<br>
我们知道一个角色有多个属于它的状态，而这些状态不可能是游离态存在内存中，我们必须用某些方式把这个角色的所有状态管理起来，我们或许可以这样做：找个人畜无害的位置，添加一个静态类，存储玩家的所有状态：<br>
<br>
export class PlayerStates &#123;<br>
<br>
static idle: IdleState;<br>
<br>
static jumping: JumpingState;<br>
<br>
static ducking: DuckingState;<br>
<br>
static diving: DivingState;<br>
<br>
//...<br>
<br>
&#125;<br>
<br>
这样玩家就可以切换状态：<br>
<br>
export default class Player_Idle extends StateBase &#123;<br>
<br>
onEnter(): void &#123; &#125;<br>
<br>
onExit(): void &#123; &#125;<br>
<br>
onUpdate(dt: any): void &#123; &#125;<br>
<br>
onKeyDown(event: any): void &#123;<br>
<br>
switch (event.keyCode) &#123;<br>
<br>
case cc.macro.KEY.space:<br>
<br>
// 跳跃状态<br>
<br>
this._role._state = PlayerStates.JumpingState;<br>
<br>
break;<br>
<br>
case cc.macro.KEY.down:<br>
<br>
// 卧倒状态<br>
<br>
this._role._state = PlayerStates.DuckingState;<br>
<br>
break;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
onKeyUp(event: any): void &#123; &#125;<br>
<br>
&#125;<br>
<br>
这有问题吗？没有问题。但现在优化到了这一步，我不甘心这么做，因为这依旧是一个耦合较高的实现方法。这样的实现方式意味着每个角色都需要一个单独的类来存放状态合集，当一个游戏中存在多个角色，多个职业的时候，这个做法就相当繁琐。<br>
<br>
那么这个问题有没有突破口呢？当然有，用容器装起来！既解决了耦合问题，也保留了之前的方式的所有灵活性，只需要往容器中注册一个状态就可以了。<br>
<br>
protected _mapStates: Map<string, StateBase> = new Map();   //角色状态集合<br>
<br>
<strong><font color="#de5650">将现有的代码模块化</font></strong><br>
<br>
现在整理一下我们所实现的部分：<br>
<br>
多个状态继承自一个状态基类，实现相同的接口。<br>
<br>
角色类中定义了该角色当前状态的变量 _state 。<br>
<br>
用一个容器 _mapStates 存储某个角色的状态合集。<br>
<br>
我觉着功能已经差不多完善了，将处理状态相关的变量聚合到一个类中，将角色类彻底放空，同时像一般的管理器一样，实现对于状态类的增删查改，画个框架图便于理解。<br>
<br>
<div align="center">
<img aid="1030904" zoomfile="https://di.gameres.com/attachment/forum/202202/16/112914ha5nf6aaip56pxpj.jpg" data-original="https://di.gameres.com/attachment/forum/202202/16/112914ha5nf6aaip56pxpj.jpg" width="584" id="aimg_1030904" inpost="1" src="https://di.gameres.com/attachment/forum/202202/16/112914ha5nf6aaip56pxpj.jpg" referrerpolicy="no-referrer">
</div><br>
Animator.ts<br>
<br>
/**动画机类，用于管理单个角色的状态 */<br>
<br>
export default class Animator &#123;<br>
<br>
protected _mapStates: Map<string, StateBase> = new Map();   //角色状态集合<br>
<br>
protected _state: StateBase | null = null;                  //角色当前状态<br>
<br>
/**<br>
<br>
* 注册状态<br>
<br>
* @param key 状态名<br>
<br>
* @param state 状态对象<br>
<br>
* @returns<br>
<br>
*/<br>
<br>
regState(key: string, state: StateBase): void &#123;<br>
<br>
if ('' === key) &#123;<br>
<br>
cc.error('The key of state is empty');<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
if (null == state) &#123;<br>
<br>
cc.error('Target state is null');<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
if (this._mapStates.has(key))<br>
<br>
return;<br>
<br>
this._mapStates.set(key, state);<br>
<br>
&#125;<br>
<br>
/**<br>
<br>
* 删除状态<br>
<br>
* @param key 状态名<br>
<br>
* @returns<br>
<br>
*/<br>
<br>
delState(key: string): void &#123;<br>
<br>
if ('' === key) &#123;<br>
<br>
cc.error('The key of state is empty');<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
this._mapStates.delete(key);<br>
<br>
&#125;<br>
<br>
/**<br>
<br>
* 切换状态<br>
<br>
* @param key 状态名<br>
<br>
* @returns<br>
<br>
*/<br>
<br>
switchState(key: string) &#123;<br>
<br>
if ('' === key) &#123;<br>
<br>
cc.error('The key of state is empty.');<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
if (this._state) &#123;<br>
<br>
if (this._state == this._mapStates.get(key))<br>
<br>
return;<br>
<br>
this._state.onExit();<br>
<br>
&#125;<br>
<br>
this._state = this._mapStates.get(key);<br>
<br>
if (this._state)<br>
<br>
this._state.onEnter();<br>
<br>
else<br>
<br>
cc.warn(`Animator error: state '$&#123;key&#125;' not found.`);<br>
<br>
&#125;<br>
<br>
/**获取状态机内所有状态 */<br>
<br>
getStates(): Map<string, StateBase> &#123;<br>
<br>
return this._mapStates;<br>
<br>
&#125;<br>
<br>
/**获取当前状态 */<br>
<br>
getCurrentState(): StateBase &#123;<br>
<br>
return this._state;<br>
<br>
&#125;<br>
<br>
/**当前状态更新函数 */<br>
<br>
onUpdate(dt: any) &#123;<br>
<br>
if (!this._state) &#123;<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
if (!this._state.onUpdate) &#123;<br>
<br>
cc.warn('Animator onUpdate: state has not update function.');<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
this._state.onUpdate(dt);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
接下来在角色类中只需要定义一个 Animator 类的变量，并向其中注册我们需要的状态，再继续执行之前的逻辑代码：<br>
<br>
Player.ts<br>
<br>
export default class Player &#123;<br>
<br>
private _animator: Animator| null = null;<br>
<br>
onInit() &#123;<br>
<br>
// 状态机注册<br>
<br>
this._animator = new Animator();<br>
<br>
if (this._animator) &#123;<br>
<br>
this._animator.regState('Idle', new IdleState(this));<br>
<br>
this._animator.regState('Jumping', new JumpingState(this));<br>
<br>
this._animator.regState('Ducking', new DuckingState(this));<br>
<br>
this._animator.regState('Diving', new DivingState(this));<br>
<br>
&#125;<br>
<br>
// 按键响应事件绑定<br>
<br>
cc.systemEvent.on(cc.SystemEvent.EventType.KEY_DOWN, this.onKeyDown, this);<br>
<br>
cc.systemEvent.on(cc.SystemEvent.EventType.KEY_UP, this.onKeyUp, this);<br>
<br>
this.schedule(this.onUpdate);<br>
<br>
&#125;<br>
<br>
onEnter(params?: any) &#123; &#125;<br>
<br>
onUpdate(dt: any) &#123;<br>
<br>
this._animator.onUpdate(dt);<br>
<br>
&#125;<br>
<br>
onKeyDown(event: any) &#123;<br>
<br>
let state = this._animator.getCurrentState();<br>
<br>
if (state) &#123;<br>
<br>
state.onKeyDown(event);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
onKeyUp(event: any) &#123;<br>
<br>
let state = this._animator.getCurrentState();<br>
<br>
if (state) &#123;<br>
<br>
state.onKeyUp(event);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
当然，可以选择做一些拓展的工作，让状态机也被管理起来：<br>
<br>
AnimatorManager.ts<br>
<br>
/**动画机管理器 */<br>
<br>
export default class AnimatorManager &#123;<br>
<br>
//单例<br>
<br>
private static _instance: AnimatorManager | null = null;<br>
<br>
public static instance(): AnimatorManager &#123;<br>
<br>
if (!this._instance) &#123;<br>
<br>
this._instance = new AnimatorManager();<br>
<br>
&#125;<br>
<br>
return this._instance;<br>
<br>
&#125;<br>
<br>
private _mapAnimators: Map<string, Animator> = new Map<string, Animator>();<br>
<br>
/**<br>
<br>
* 获取动画机，若不存在则新建并返回<br>
<br>
* @param key 动画机名<br>
<br>
* @returns 动画机<br>
<br>
*/<br>
<br>
getAnimator(key: string): Animator | null &#123;<br>
<br>
if ("" == key) &#123;<br>
<br>
cc.error("AnimatorManager error: The key of Animator is empty");<br>
<br>
&#125;<br>
<br>
let anim: Animator | null = null;<br>
<br>
if (!this._mapAnimators.has(key)) &#123;<br>
<br>
anim = new Animator();<br>
<br>
this._mapAnimators.set(key, anim);<br>
<br>
&#125;<br>
<br>
else &#123;<br>
<br>
anim = this._mapAnimators.get(key);<br>
<br>
&#125;<br>
<br>
return anim;<br>
<br>
&#125;<br>
<br>
/**<br>
<br>
* 删除动画机<br>
<br>
* @param key 动画机名<br>
<br>
*/<br>
<br>
delAnimator(key: string) &#123;<br>
<br>
this._mapAnimators.delete(key);<br>
<br>
&#125;<br>
<br>
/** 清空动画机 */<br>
<br>
clearAnimator() &#123;<br>
<br>
this._mapAnimators.clear();<br>
<br>
&#125;<br>
<br>
/**动画机状态更新 */<br>
<br>
onUpdate(dt: any) &#123;<br>
<br>
this._mapAnimators.forEach((value: Animator, key: string) => &#123;<br>
<br>
value.onUpdate(dt);<br>
<br>
&#125;);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
这样角色类的 new 操作就被集中到了管理类，在 Player.ts 中也就不需要再 new 了：<br>
<br>
// 状态机注册<br>
<br>
this._animator = AnimatorManager.instance().getAnimator("player");<br>
<br>
if (this._animator) &#123;<br>
<br>
this._animator.regState('Idle', new IdleState(this));<br>
<br>
this._animator.regState('Jumping', new JumpingState(this));<br>
<br>
this._animator.regState('Ducking', new DuckingState(this));<br>
<br>
this._animator.regState('Diving', new DivingState(this));<br>
<br>
&#125;<br>
<br>
<strong><font color="#de5650">成品</font></strong><br>
<br>
最终的角色状态切换效果通过如下代码实现，干净整洁：<br>
<br>
<div align="center"><font size="2">
<img aid="1030905" zoomfile="https://di.gameres.com/attachment/forum/202202/16/113217cmb6kmrryuk7f2pk.jpg" data-original="https://di.gameres.com/attachment/forum/202202/16/113217cmb6kmrryuk7f2pk.jpg" width="600" id="aimg_1030905" inpost="1" src="https://di.gameres.com/attachment/forum/202202/16/113217cmb6kmrryuk7f2pk.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">注：this.getController() 为控制移动的模块，与该系统无关</font></div><br>
即使状态机有这些常见的扩展，它们也受到一些限制。这里只是记录下我的解决方式，意为抛砖引玉，欢迎大家点击文末【阅读原文】到论坛专贴一起交流！<br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/st0KdsRpSb-ekoJNcp_Ruw</font><br>
<br>
<br>
  
</div>
            