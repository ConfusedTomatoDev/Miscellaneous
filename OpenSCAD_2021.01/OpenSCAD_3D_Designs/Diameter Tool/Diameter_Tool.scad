// ============================
// PARAMETERS
// ============================

// ---Plate dimensions
//
rect_width = 150;
rect_height = 30;
rect_thickness = 5;

// ---Hole configuration
//
num_holes = 10;
start_diameter = 10;
end_diameter = 1;
margin = 10;
hole_diameter_correction = 0.5;

// ---Text configuration
//
title_text = "Diameter Test Tool";
text_space = 2.3;
text_height = 1.5;
text_embed = 2.3;
text_thickness = 0.3;
font_size = 5;
text_color = [0.2, 0.6, 1];

// ---Feature toggles
//
bold_off = true;
embosed = true;
show_mm = false;

// ============================
// CALCULATED SPACING
// ============================

hole_spacing = (rect_width - 2 * margin) / (num_holes - 1);

// ============================
// MAIN MODEL
// ============================

translate([0, 0, rect_thickness / 2]) {

    if (!embosed) {
        // ========== ENGRAVED MODE ==========
        difference() {
            // Base with holes
            cube([rect_width, rect_height, rect_thickness], center = true);
            for (i = [0 : num_holes - 1]) {
                d = start_diameter + (end_diameter - start_diameter) * i / (num_holes - 1) + hole_diameter_correction;
                x_pos = -rect_width / 2 + margin + i * hole_spacing;
                translate([x_pos, 0, 0])
                    cylinder(h = rect_thickness + 1, d = d, center = true);
            }

            // Engraved hole labels
            for (i = [0 : num_holes - 1]) {
                d = start_diameter + (end_diameter - start_diameter) * i / (num_holes - 1) + hole_diameter_correction;
                d_int = floor(d);
                x_pos = -rect_width / 2 + margin + i * hole_spacing;
                y_pos = -rect_height / text_space + font_size / text_space;
                z_pos = rect_thickness / 1.5 - text_height; // 1.5 is the engrave depth.

                translate([x_pos, y_pos, z_pos]) 
                    color(text_color)
                    {
                        if (bold_off) {
                            if (show_mm) {
                                linear_extrude(height = text_height)
                                    text(str(d_int, " mm"), size = font_size, halign = "center", valign = "center", font = "Liberation Sans:style=Bold");
                            } else {
                            linear_extrude(height = text_height)
                                    text(str(d_int), size = font_size, halign = "center", valign = "center", font = "Liberation Sans:style=Bold");
                            }
                        } else {
                            if (show_mm) {
                                linear_extrude(height = text_height)
                                    offset(r = text_thickness)
                                        text(str(d_int, " mm"), size = font_size, halign = "center", valign = "center");
                        } else {
                            linear_extrude(height = text_height)
                                offset(r = text_thickness)
                                    text(str(d_int), size = font_size, halign = "center", valign = "center");
                        }
                    }
                }
            }

            // Engraved title
            header_label = show_mm ? title_text : str(title_text, " (mm)");
            header_x = 0;
            //header_y = rect_height / 2 - font_size * 0.75;
            header_y = rect_height / 2 / text_space + font_size / text_space;
            header_z = rect_thickness / 1.5 - text_height;  // 1.5 is the engrave depth.

            translate([header_x, header_y, header_z]) 
                color(text_color)
                {
                    if (bold_off) {
                        linear_extrude(height = text_height)
                            text(header_label, size = font_size + 1, halign = "center", valign = "center", font = "Liberation Sans:style=Bold");
                    } else {
                    linear_extrude(height = text_height)
                        offset(r = text_thickness)
                            text(header_label, size = font_size + 1, halign = "center", valign = "center");
                }
            }
        }

    } else {
        // ========== EMBOSSED MODE ==========
        difference() {
            // Base with holes
            cube([rect_width, rect_height, rect_thickness], center = true);
            for (i = [0 : num_holes - 1]) {
                d = start_diameter + (end_diameter - start_diameter) * i / (num_holes - 1) + hole_diameter_correction;
                x_pos = -rect_width / 2 + margin + i * hole_spacing;
                translate([x_pos, 0, 0])
                    cylinder(h = rect_thickness + 1, d = d, center = true);
            }
        }

        // Embossed hole labels
        for (i = [0 : num_holes - 1]) {
            d = start_diameter + (end_diameter - start_diameter) * i / (num_holes - 1) + hole_diameter_correction;
            d_int = floor(d);
            x_pos = -rect_width / 2 + margin + i * hole_spacing;
            y_pos = -rect_height / text_space + font_size / text_space;
            //z_pos = rect_thickness / 2.2;
            z_pos = rect_thickness / text_embed;

            translate([x_pos, y_pos, z_pos])
                color(text_color)
                {
                    if (bold_off) {
                        if (show_mm) {
                            linear_extrude(height = text_height)
                                text(str(d_int, " mm"), size = font_size, halign = "center", valign = "center", font = "Liberation Sans:style=Bold");
                        } else {
                            linear_extrude(height = text_height)
                                text(str(d_int), size = font_size, halign = "center", valign = "center", font = "Liberation Sans:style=Bold");
                        }
                    } else {
                        if (show_mm) {
                            linear_extrude(height = text_height)
                                offset(r = text_thickness)
                                    text(str(d_int, " mm"), size = font_size, halign = "center", valign = "center");
                        } else {
                            linear_extrude(height = text_height)
                                offset(r = text_thickness)
                                    text(str(d_int), size = font_size, halign = "center", valign = "center");
                        }
                    }
                }
        }

        // Embossed title
        header_label = show_mm ? title_text : str(title_text, " (mm)");
        header_x = 0;
        //header_y = rect_height / text_space - font_size * 0.75;
        header_y = rect_height / 2 / text_space + font_size / text_space;
        header_z = rect_thickness / text_embed;

        translate([header_x, header_y, header_z])
            color(text_color)
            {
                if (bold_off) {
                    linear_extrude(height = text_height)
                        text(header_label, size = font_size + 1, halign = "center", valign = "center", font = "Liberation Sans:style=Bold");
                } else {
                    linear_extrude(height = text_height)
                        offset(r = text_thickness)
                            text(header_label, size = font_size + 1, halign = "center", valign = "center");
                }
            }
    }
}
