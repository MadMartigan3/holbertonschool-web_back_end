-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (COALESCE(NULLIF(`split`, 0), 2024) - `formed`) AS lifespan FROM metal_bands
WHERE `style` LIKE '%Glam rock%' AND `formed` IS NOT NULL ORDER BY lifespan DESC;
