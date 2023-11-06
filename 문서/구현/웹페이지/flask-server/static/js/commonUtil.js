/**
 * 공통
 */
/******    20210427 수정  begin    ********/

$(document).ready(function(){
	/*  gnb  */
	$('.web-nav li').mouseenter(function(){
		$('.menu-frame').addClass("on");
		$('.menu-frame').slideDown(600);
		
		$('.menu-wrap').addClass("on");
		$('.menu-wrap').slideDown(200);
	});

	$('.nav-wrap').mouseleave(function(){
		$('.menu-frame').removeClass("on");
		$('.menu-frame').slideUp(600);
		
		$('.menu-wrap').removeClass("on");
		$('.menu-wrap').slideUp(200);
	});
	
	$('.menu-wrap ul').each(function(i,e){
		$(e).hover(function(){
			$('.web-nav li').eq(i).addClass('on');
		},function(){
			$('.web-nav li').removeClass('on');
		})
	});
	
	
	/** 키보드 웹접근성 조치 */
	$('.web-nav li').children("a").focus(function(){
		$('.menu-frame').addClass("on");
		$('.menu-frame').slideDown(600);
		
		$('.menu-wrap').addClass("on");
		$('.menu-wrap').slideDown(200);
	});
	
	// .web-nav li:last-child > .menu-wrap ul li:last-child > a
	$('.menu-wrap ul li:last-child > a').blur(function(){
		$('.menu-frame').removeClass("on");
		$('.menu-frame').slideUp(600);
		
		$('.menu-wrap').removeClass("on");
		$('.menu-wrap').slideUp(200);
	});
	
	
	/* 달력  
	$("#datepicker").datepicker({
		changeMonth: true,
		changeYear: true
	});

	*/
	
	
	
	/******    20210427 수정   end    ********/

	
	/******    20210407 모바일 로고 위치 계산  begin    ********/
	$('.m-logo').css({
		"left": (($(window).width()-$('.m-logo').width())/2+$(window).scrollLeft())+'px'
	});

/******   20210407 모바일 로고 위치 계산  end  ********/


	/*  모바일 메뉴  */
	
	

	/*  모바일 메뉴 height  */
	var h = window.innerHeight - $('.m-nav-info').height() - $('.m-member').height() - $('.m-aside').height() - 25;
	$('.m-lnb').height(h);
	/*  20210325 추가 begin  */
	$('.m-lnb').css('overflow-y','auto');
	/*  20210325 추가 end  */
	
	
	/*  input width  */
	var inputSocialW = $('#nomalCheck ul li input.Social-num').width() *2 + $('.name-check ul li span').outerWidth() +8;
	$('#nomalCheck ul li input.input-box').width(inputSocialW);
	
	var inputBuisnessW = $('#buisnessCheck ul li input.buisness-num').width()*3 + $('.name-check ul li span').outerWidth() +35;
	$('#buisnessCheck ul li input.input-box').width(inputBuisnessW);
	
	
	/*  상세내용 보기 label 높이  */
	var labelH = $('.view-form >ul >li.file-link >.input-form').height();
	/*  20210325 추가 및 수정 begin  */
		if(window.innerWidth>=768){
			if(labelH<47){
				$('.view-form ul >.file-link >label').css('line-height',47+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}else{
				$('.view-form ul >.file-link >label').css('line-height',labelH+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}
		}else{
			if(labelH<34){
				$('.view-form ul >.file-link >label').css('line-height',34+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}else{
				$('.view-form ul >.file-link >label').css('line-height',labelH+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}
		}
	/*  20210325 추가 및 수정 end  */
	
	
	/*  모바일 게시판 width 계산  */
	var mboardWidth = $('.board-tab >ul >li:nth-child(1)').width() + $('.board-tab >ul >li:nth-child(2)').width() + $('.board-tab >ul >li:nth-child(3)').width();
	$('.m-board-box').innerWidth(mboardWidth);
	
	
	/* textarea width  */
	var areaWidth = $('.regist-form ul').width() - 45;
	$('.editor').width(areaWidth);
	
	
	$(window).resize(function () {
		var h = window.innerHeight - $('.m-nav-info').height() - $('.m-member').height() - $('.m-aside').height() - 25;
		$('.m-lnb').height(h);
		/*  20210325 추가 begin  */
		$('.m-lnb').css('overflow-y','auto');
		/*  20210325 추가 end  */
		
		var inputSocialW = $('#nomalCheck ul li input.Social-num').width() *2 + $('.name-check ul li span').outerWidth() +8;
		$('#nomalCheck ul li input.input-box').width(inputSocialW);
		
		var inputBuisnessW = $('#buisnessCheck ul li input.buisness-num').width()*3 + $('.name-check ul li span').outerWidth() +35;
		$('#buisnessCheck ul li input.input-box').width(inputBuisnessW);
		
		var labelH = $('.view-form >ul >li.file-link >.input-form').height();
		$('.view-form ul >.file-link >label').height(labelH);
		/*  20210325 추가 및 수정 begin  */
		if(window.innerWidth>=768){
			if(labelH<47){
				$('.view-form ul >.file-link >label').css('line-height',47+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}else{
				$('.view-form ul >.file-link >label').css('line-height',labelH+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}
		}else{
			if(labelH<34){
				$('.view-form ul >.file-link >label').css('line-height',34+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}else{
				$('.view-form ul >.file-link >label').css('line-height',labelH+'px');
				$('.view-form ul >.file-link >label').height(labelH);
			}
		}
	/*  20210325 추가 및 수정 end  */
		
		
		
		var mboardWidth = $('.board-tab >ul >li:nth-child(1)').width() + $('.board-tab >ul >li:nth-child(2)').width() + $('.board-tab >ul >li:nth-child(3)').width();
		$('.m-board-box').innerWidth(mboardWidth);
		
		
		var areaWidth = $('.editor-wrap').width();
		$('.qna-area').width(areaWidth);
		
		
		/*  20210407 추가 begin  */
		$('.m-logo').css({
			"left": (($(window).width()-$('.m-logo').width())/2+$(window).scrollLeft())+'px'
		});
		/*  20210407 추가 end  */
		
	});

	
	
	

	$('.m-menu').on('click', function(){
		$('.layer-bg').show(); 
		$('.m-nav').show().animate({
			right:0
		});
		$('body').css('overflow-y','hidden');
		//$('.m-lnb').height(h);
		//$('.m-lnb').css('overflow-y','auto');
	});
	$('#closeBtn').on('click', function(){
		$('.layer-bg').hide(); 
		$('.m-nav').animate({
			right: '-' + 65 + '%'},
			function(){
				$('.m-nav').hide(); 
		});
		$('body').css('overflow-y','auto');
	});
	
	/******  20210420 추가  (모바일/tablet 메뉴 여백 클릭시 메뉴 닫힘) **********/
	$('.layer-bg').on('click', function(){
		$('.layer-bg').hide(); 
		$('.m-nav').animate({
			right: '-' + 65 + '%'},
			function(){
				$('.m-nav').hide(); 
		});
		$('body').css('overflow-y','auto');
	});
	/******  20210420 추가  (모바일/tablet 메뉴 여백 클릭시 메뉴 닫힘) **********/
	
	
	$('.sub-lnb li a').on('click', function(){
		$('.layer-bg').hide(); 
		$('.m-nav').animate({
			right: '-' + 65 + '%'},
			function(){
				$('.m-nav').hide(); 
		});
		$('body').css('overflow-y','auto');
	});


	

	/*   2depth   */
	$('.m-lnb ul li a').click(function(){
		//$(this).next('.m-lnb ul li>.sub-lnb').slideToggle(400);
		$(this).next('.m-lnb ul li>.sub-lnb').slideDown(400);
		$('.m-lnb ul li a').not(this).next().slideUp(400);
		
		return false;
	});
	
	$('.m-lnb ul li a').eq(0).trigger("click");
	
	
	
	
	/*   약관동의   */
	$('.agree-wrap ul li').click(function(e){
		if(window.outerWidth<=1024 && !$(e.target).hasClass("checkbox")){
			//$(this).next('.m-lnb ul li>.sub-lnb').slideToggle(400);
			$(this).children('.agree-wrap ul li>.policy-section').slideDown(400);
			$(this).addClass('on');
			$('.agree-wrap ul li').not(this).children('.agree-wrap ul li>.policy-section').slideUp(400);
			$('.agree-wrap ul li').not(this).removeClass('on');
		
			return false;
		}
	
		//$('.agree-wrap ul li').eq(0).trigger("click");
	});

	
	/*   mobile 정보입력   */
	
		/*   (필수)자원정보   */
//	$('#resourceForm >.form-label').click(function() {
//		if(window.outerWidth<=1024){	
//			$(this).next('#resourceForm >.info-form').slideToggle(600);
//			$(this).parent().toggleClass('on');	
//		}
//	
//	});
//	
//	
//	/*   서울시로 이전 중일때 (선택)정보   */
//	$('#resourceSeoulForm >.form-label').click(function() {
//		if(window.outerWidth<=1024){
//			$(this).next('#resourceSeoulForm >.info-form').slideToggle(600);
//			$(this).parent().toggleClass('on');	
//		}
//	
//	});
//	
//	
//	
//	
//	/*   (선택)정보   */
//	$('#selection_div >.form-label').click(function() {
//		if(window.outerWidth<=1024){
//			$(this).next('#selection_div >.info-form').slideToggle(600);
//			$(this).parent().toggleClass('on');	
//		}
//	
//	});
//	
//	
//	
//	/*   인증서 등록   */
//	$('#certifForm >.form-label').click(function() {
//		if(window.outerWidth<=1024){
//			$(this).next('#certifForm >.info-form').slideToggle(600);
//			$(this).parent().toggleClass('on');	
//		}
//	
//	});
	
	
	
	/*   faq begin */
	$('.faq-board > ul >.faq-list >h2').click(function(){
		$(this).next('.faq-board > ul >.faq-list >.answer-wrap').slideDown(400);
		$(this).parent().addClass('on');
		$('.faq-board > ul >.faq-list >h2').not(this).next().slideUp(400);
		$('.faq-board > ul >.faq-list >h2').not(this).parent().removeClass('on');

		return false;
	});
	//$('.faq-board > ul >.faq-list >h2').eq(0).trigger("click");

	/*   faq end */
	
});



// 현재 열려있는 레이어팝업 변수
var currPopup = null;
		
/*레이어팝업 열기*/
function layerPopupOpen(){
	
	$("#popupBack").addClass("pop-layer");
	$('body').css('overflow','hidden');
	$('.pop-wrap').css({
		"top": (($(window).height()-$('.pop-wrap').outerHeight())/2)+'px',
		"left": (($(window).width()-$('.pop-wrap').outerWidth())/2)+'px'
	});
	$('#popupDiv').show();
	
	$(".pop-header").find("button").focus();
}

/*레이어팝업 닫기*/		
function layerPopupClose(){
	
	$("#popupBack").removeClass("pop-layer");
	
	$('.pop-wrap').css({
		"top": '',
		"left": ''
	});
	
	$("#popupDiv").empty();
	$('#popupDiv').hide();
	$("#popupDiv").removeClass("small-pop");
	$('body').css('overflow','auto');
	
	if(currPopup != null){
		currPopup.focus();
	}
	
	currPopup = null;	// 현재팝업 초기화
}		


// 로딩바 열기
function openLoading(){
	$(".loading-bar").css("display","");
}

// 로딩바 닫기
function closeLoading(){
	$(".loading-bar").css("display","none");
}

//인풋에 영어, 숫자만 가능하도록
function onlyEngNum(e){
	e.value = e.value.replace(/[^A-Za-z0-9]/gi,'');
}

// 인풋 타입 넘버일 때 maxlength 체크 함수(onInput에 걸기)
function maxLengthCheck(object){
	if(object.value.length > object.maxLength){
		object.value = object.value.slice(0,object.maxLength);
	}
}

// 개인정보 마스킹 함수
//let maskingFunc = {
//		
//		// 들어온 글자 값 체크
//		checkNull : function(str){
//			if(typeof str == "undefined" || str == null || str == ""){
//				return true;
//			}else{
//				return false;
//			}
//		},
//		
//		// 들어온 글자 모두 마스킹
//		any : function(str){
//			let originStr = str;
//			let maskingStr;
//			
//			if(this.checkNull(originStr)){
//				return originStr;
//			}
//			
//			maskingStr = originStr.replace(/(?<=.{0})./gi,"*");
//			return maskingStr;
//		},
//		
//		// 이름 마스킹
//		name : function(str){
//			let originStr = str;
//			let maskingStr;
//			let strLength;
//			
//			if(this.checkNull(originStr)){
//				return originStr;
//			}
//			
//			strLength = originStr.length;
//			
//			if(strLength < 3){
//				maskingStr = originStr.replace(/(?<=.{1})./gi,"*");
//			}else{
//				maskingStr = originStr.replace(/(?<=.{2})./gi,"*");
//			}
//			
//			return maskingStr;
//		},
//		
//		// 이메일 마스킹
//		email : function(str){
//			let originStr = str;
//			let emailStr = originStr.match(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi);
//			let strLength;
//			
//			if(this.checkNull(originStr) || this.checkNull(emailStr)){
//				return originStr;
//			}else{
//				strLength = emailStr.toString().split('@')[0].length-3;
//				return originStr.toString().replace(new RegExp('.(?=.{0,'+strLength+'}@)','g'),'*');
//			}
//		},
//}



		
			