@objects
   header          css    .s-header
   menu            css    .s-toolbar
   content         css    .s-app-wrapper__sections
   side-panel      css    .s-intro__sidebar
   footer          css    .s-panel__footer
   
= Header =
    header:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible

= Menu =
    menu:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible

= Content =
    content:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible

= Side Panel =
    side-panel:
      @on desktop 
          width 300px
      @on tablet 
          width 300px
      @on mobile 
          width 100 % of screen/width

= Footer =
    footer:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible
